from fastapi import status
from sqlalchemy.orm import Session
from server.database import get_db, Base, engine
from server.apps.auth.schemas import UserCreate
from server.apps.auth.service import create_user

# 테스트 데이터베이스 설정
Base.metadata.create_all(bind=engine)

def test_signup(test_client):
    response = test_client.post("/auth/signup", json={
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == "testuser@example.com"

def test_login(test_client):
    # 사전 사용자 생성
    db: Session = next(get_db())
    user = UserCreate(username="testuser", email="testuser@example.com", password="testpassword")
    create_user(db, user)

    response = test_client.post("/auth/login", data={
        "username": "testuser@example.com",
        "password": "testpassword"
    })
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()

def test_logout(test_client):
    # ��그인하여 토큰 획득
    response = test_client.post("/auth/login", data={
        "username": "testuser@example.com",
        "password": "testpassword"
    })
    token = response.json()["access_token"]

    # 로그아웃 테스트
    response = test_client.post("/auth/logout", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == "Successfully logged out" 