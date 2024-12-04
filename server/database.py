from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from server.config import settings
from sqlalchemy.orm import Session


# 데이터베이스 엔진 생성
engine = create_async_engine(settings.DATABASE_URL, echo=True)

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
