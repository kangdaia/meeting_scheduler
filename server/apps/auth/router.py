from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from . import schemas, service, utils
from server.database import get_db, redis_client
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config
from starlette.responses import RedirectResponse
from server.config import settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# OAuth 설정
oauth = OAuth()
providers = settings.oauth_providers

for provider_name, provider_config in providers.items():
    oauth.register(
        name=provider_name,
        **provider_config
    )

@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db=db, user=user)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = service.get_user_by_email(db, email=form_data.username)
    if not user or not utils.pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = utils.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
def logout(token: str = Depends(oauth2_scheme)):
    redis_client.set(token, "blacklisted")
    return {"message": "Successfully logged out"}


@router.get("/login/{provider_name}")
async def login_via_provider(request: Request, provider_name: str):
    if not providers[provider_name]:
        raise HTTPException(status_code=400, detail=f"{provider_name} OAuth is not configured")
    redirect_uri = request.url_for("auth_callback")
    return await oauth[provider_name].authorize_redirect(request, redirect_uri)


@router.get("/auth/callback")
async def auth_callback(request: Request, provider_name: str):
    if not providers[provider_name]:
        raise HTTPException(status_code=400, detail=f"{provider_name} OAuth is not configured")
    token = await oauth[provider_name].authorize_access_token(request)
    user_info = await oauth[provider_name].parse_id_token(request, token)
    if not user_info:
        raise HTTPException(status_code=400, detail="Failed to fetch user info")
    # 사용자 정보를 사용하여 로그인 처리
    return {"email": user_info["email"], "name": user_info["name"]}
