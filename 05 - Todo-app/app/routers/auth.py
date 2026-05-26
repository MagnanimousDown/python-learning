from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.models.user_model import User

from app.schemas.auth_schema import (
    UserCreate,
    UserLogin,
    TokenResponse
)

from app.utils.hashing import (
    hash_password,
    verify_password
)

from app.utils.jwt import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/signup")
async def signup(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    
    hashed_password = hash_password(user.password)

    new_user = User(
        username = user.username,
        password = hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created successfully"
    }

@router.post("/signin", response_model=TokenResponse)
async def signin(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    is_valid = verify_password(
        user.password,
        existing_user.password
    )

    if not is_valid:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    access_token = create_access_token({
        "sub": existing_user.username
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }