from sqlalchemy import Column, Integer, String, UUID
from server.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, unique=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
