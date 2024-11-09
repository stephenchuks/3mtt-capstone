from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

router = APIRouter()

@router.post("/users/")
def create_user(name: str, email: str, password: str, db: Session = Depends(get_db)):
    new_user = User(name=name, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": "Sample User"}

