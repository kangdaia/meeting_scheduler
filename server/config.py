from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


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

    class Config:
        env_file = ".env"
        case_sensitive = True


# 설정 인스턴스 생성
settings = Settings()
