from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field
import logging


class EndpointFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().find("/health") == -1


logging.getLogger("uvicorn.access").addFilter(EndpointFilter())


class Settings(BaseSettings):
    # 기본 애플리케이션 설정
    APP_NAME: str = "FastAPI App"
    DEBUG: bool = Field(default=False, description="디버그 모드 활성화 여부")
    
    # 서버 설정
    HOST: str = Field(default="0.0.0.0", description="서버 호스트")
    PORT: int = Field(default=8000, description="서버 포트")
    
    # 데이터베이스 설정
    DATABASE_URL: Optional[str] = Field(
        default="sqlite:///./sql_app.db",
        description="데이터베이스 연결 문자열"
    )
    
    # JWT 설정
    SECRET_KEY: str = Field(
        default="your-secret-key",
        description="JWT 토큰 암호화에 사용되는 비밀키"
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=30,
        description="액세스 토큰 만료 시간(분)"
    )
    
    # CORS 설정
    ALLOWED_ORIGINS: list[str] = Field(
        default=["http://localhost:5173"],
        description="CORS 허용 도메인 목록"
    )

    # OAuth 기본 설정
    ENABLE_OAUTH_SIGNUP: bool = Field(
        default=False,
        description="OAuth 회원가입 활성화 여부"
    )
    OAUTH_MERGE_ACCOUNTS_BY_EMAIL: bool = Field(
        default=False,
        description="이메일 기반 계정 병합 여부"
    )

    # Google OAuth 설정
    GOOGLE_CLIENT_ID: str = Field(default="", description="Google OAuth 클라이언트 ID")
    GOOGLE_CLIENT_SECRET: str = Field(default="", description="Google OAuth 클라이언트 시크릿")
    GOOGLE_OAUTH_SCOPE: str = Field(
        default="openid email profile",
        description="Google OAuth 스코프"
    )
    GOOGLE_REDIRECT_URI: str = Field(default="", description="Google OAuth 리다이렉트 URI")

    # Microsoft OAuth 설정
    MICROSOFT_CLIENT_ID: str = Field(default="", description="Microsoft OAuth 클라이언트 ID")
    MICROSOFT_CLIENT_SECRET: str = Field(default="", description="Microsoft OAuth 클라이언트 시크릿")
    MICROSOFT_CLIENT_TENANT_ID: str = Field(default="", description="Microsoft 테넌트 ID")
    MICROSOFT_OAUTH_SCOPE: str = Field(
        default="openid email profile",
        description="Microsoft OAuth 스코프"
    )
    MICROSOFT_REDIRECT_URI: str = Field(default="", description="Microsoft OAuth 리다이렉트 URI")

    # OpenID Connect 설정
    OAUTH_CLIENT_ID: str = Field(default="", description="OIDC 클라이언트 ID")
    OAUTH_CLIENT_SECRET: str = Field(default="", description="OIDC 클라이언트 시크릿")
    OPENID_PROVIDER_URL: str = Field(default="", description="OIDC 프로바이더 URL")
    OPENID_REDIRECT_URI: str = Field(default="", description="OIDC 리다이렉트 URI")
    OAUTH_SCOPES: str = Field(
        default="openid email profile",
        description="OIDC 스코프"
    )
    OAUTH_PROVIDER_NAME: str = Field(default="SSO", description="OIDC 프로바이더 이름")

    # OAuth 클레임 설정
    OAUTH_USERNAME_CLAIM: str = Field(default="name", description="사용자 이름 클레임")
    OAUTH_PICTURE_CLAIM: str = Field(default="picture", description="프로필 사진 클레임")
    OAUTH_EMAIL_CLAIM: str = Field(default="email", description="이메일 클레임")

    # OAuth 역할 관리 설정
    ENABLE_OAUTH_ROLE_MANAGEMENT: bool = Field(
        default=False,
        description="OAuth 역할 관리 활성화 여부"
    )
    OAUTH_ROLES_CLAIM: str = Field(default="roles", description="역할 클레임")
    OAUTH_ALLOWED_ROLES: list[str] = Field(
        default=["user", "admin"],
        description="허용된 역할 목록"
    )
    OAUTH_ADMIN_ROLES: list[str] = Field(
        default=["admin"],
        description="관리자 역할 목록"
    )

    @property
    def oauth_providers(self) -> dict:
        providers = {}
        
        if self.GOOGLE_CLIENT_ID and self.GOOGLE_CLIENT_SECRET:
            providers["google"] = {
                "client_id": self.GOOGLE_CLIENT_ID,
                "client_secret": self.GOOGLE_CLIENT_SECRET,
                "server_metadata_url": "https://accounts.google.com/.well-known/openid-configuration",
                "scope": self.GOOGLE_OAUTH_SCOPE,
                "redirect_uri": self.GOOGLE_REDIRECT_URI,
            }

        if all([self.MICROSOFT_CLIENT_ID, self.MICROSOFT_CLIENT_SECRET, self.MICROSOFT_CLIENT_TENANT_ID]):
            providers["microsoft"] = {
                "client_id": self.MICROSOFT_CLIENT_ID,
                "client_secret": self.MICROSOFT_CLIENT_SECRET,
                "server_metadata_url": f"https://login.microsoftonline.com/{self.MICROSOFT_CLIENT_TENANT_ID}/v2.0/.well-known/openid-configuration",
                "scope": self.MICROSOFT_OAUTH_SCOPE,
                "redirect_uri": self.MICROSOFT_REDIRECT_URI,
            }

        if all([self.OAUTH_CLIENT_ID, self.OAUTH_CLIENT_SECRET, self.OPENID_PROVIDER_URL]):
            providers["oidc"] = {
                "client_id": self.OAUTH_CLIENT_ID,
                "client_secret": self.OAUTH_CLIENT_SECRET,
                "server_metadata_url": self.OPENID_PROVIDER_URL,
                "scope": self.OAUTH_SCOPES,
                "name": self.OAUTH_PROVIDER_NAME,
                "redirect_uri": self.OPENID_REDIRECT_URI,
            }

        return providers

    class Config:
        env_file = ".env"
        case_sensitive = True

# 설정 인스턴스 생성
settings = Settings()
