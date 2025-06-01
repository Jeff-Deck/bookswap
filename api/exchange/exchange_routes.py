from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api import models

router = APIRouter(prefix="/exchange-requests", tags=["Exchange Requests"])

@router.get("/received/{user_id}")
def get_received_requests(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.ExchangeRequest).filter(models.ExchangeRequest.receiver_id == user_id).all()
