import pytest
from fastapi import status
from app.utils import hash

def test_create_user(client):
    user_data = {
        "email": "newuser@example.com",
        "password": "password123"
    }
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["email"] == user_data["email"]

def test_login_success(client):
    # First create a user
    user_data = {
        "email": "loginuser@example.com",
        "password": "password123"
    }
    client.post("/api/users/", json=user_data)
    
    # Then try to log in
    login_data = {
        "username": user_data["email"],
        "password": user_data["password"]
    }
    response = client.post("/api/login/", data=login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()

def test_login_wrong_password(client):
    # First create a user
    user_data = {
        "email": "wrongpass@example.com",
        "password": "password123"
    }
    client.post("/api/users/", json=user_data)
    
    # Then try to log in with wrong password
    login_data = {
        "username": user_data["email"],
        "password": "wrongpassword"
    }
    response = client.post("/api/login/", data=login_data)
    assert response.status_code == status.HTTP_403_FORBIDDEN 