from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.apps.auth.router import router as auth_router

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 구체적인 도메인을 지정하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 인증 라우터 추가
app.include_router(auth_router, prefix="/auth")

# 루트 엔드포인트
@app.get("/")
async def root():
    return {"message": "안녕하세요! FastAPI 서버입니다."}

