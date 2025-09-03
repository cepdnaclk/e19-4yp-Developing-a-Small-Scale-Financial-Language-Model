
import pytest
from jose import jwt
from datetime import timedelta

from code.backend import auth


def test_password_hash_and_verify():
    password = "finance123"
    hashed = auth.get_password_hash(password)
    assert auth.verify_password(password, hashed)


def test_authenticate_user_valid():
    user = auth.authenticate_user("admin", "admin123")
    assert user is not None
    assert user["role"] == "admin"


def test_authenticate_user_invalid():
    user = auth.authenticate_user("admin", "wrongpass")
    assert user is None


def test_create_and_decode_token():
    token = auth.create_access_token(
        {"sub": "testuser", "role": "viewer"},
        expires_delta=timedelta(minutes=5),
    )
    decoded = auth.decode_token(token)
    assert decoded.username == "testuser"
    assert decoded.role == "viewer"


def test_role_required_allows_role():
    checker = auth.role_required(["admin"])
    # Mock user
    class DummyUser:
        username = "admin"
        role = "admin"
    assert checker(DummyUser()) == DummyUser()
