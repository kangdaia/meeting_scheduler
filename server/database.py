from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from server.config import settings
import redis

# Redis 연결
redis_client = redis.Redis.from_url(settings.REDIS_URL)

# PostgreSQL 비동기 연결 URL로 변경
DATABASE_URL = settings.DATABASE_URL.replace(
    "postgresql+psycopg://", "postgresql+psycopg_async://"
)

# 데이터베이스 엔진 생성
engine = create_async_engine(DATABASE_URL)

# 세션 로컬 클래스 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# 베이스 클래스 생성
Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
            await db.commit()
        finally:
            await db.close()
