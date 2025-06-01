from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api import models

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/user/{user_id}")
def get_books_by_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Book).filter(models.Book.owner_id == user_id).all()
