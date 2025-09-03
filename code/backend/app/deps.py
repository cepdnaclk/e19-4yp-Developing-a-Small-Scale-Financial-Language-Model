
from fastapi import Depends
from sqlalchemy.orm import Session

from auth import get_current_user, role_required, User


# =========================
# DB SESSION (stub for now)
# =========================
def get_db():
    """
    Dependency to provide a DB session.
    Right now it's a stub (since you may not be using a DB yet).
    Later you can integrate SQLAlchemy, MongoDB, or Firebase.
    """
    db = None
    try:
        yield db
    finally:
        if db:
            db.close()


# =========================
# USER DEPENDENCIES
# =========================
async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Ensures the current user is active.
    You can extend this to check user flags in DB.
    """
    # Example: check if user is disabled in DB
    return current_user


# =========================
# ROLE SHORTCUTS
# =========================
AdminOnly = Depends(role_required(["admin"]))
AnalystOrAbove = Depends(role_required(["admin", "analyst"]))
AnyUser = Depends(role_required(["admin", "analyst", "viewer"]))
