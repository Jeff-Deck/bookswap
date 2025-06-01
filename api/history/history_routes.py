from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api import models

router = APIRouter(prefix="/history", tags=["Exchange History"])

@router.get("/user/{user_id}")
def get_exchange_history(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.ExchangeHistory).filter(
        (models.ExchangeHistory.sender_id == user_id) |
        (models.ExchangeHistory.receiver_id == user_id)
    ).all()
