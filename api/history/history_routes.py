from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api import models, schemas
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/history", tags=["Exchange History"])

@router.get("/user/{user_id}", response_model=list[schemas.ExchangeHistoryOut])
def get_exchange_history(user_id: int, db: Session = Depends(get_db)):
    history = db.query(models.ExchangeHistory).filter(
        (models.ExchangeHistory.sender_id == user_id) |
        (models.ExchangeHistory.receiver_id == user_id)
    ).all()

    enriched = []
    for h in history:
        sender = db.query(models.CustomUser).filter(models.CustomUser.id == h.sender_id).first()
        receiver = db.query(models.CustomUser).filter(models.CustomUser.id == h.receiver_id).first()

        enriched.append({
            "id": h.id,
            "book_id": h.book_id,
            "sender_id": h.sender_id,
            "sender_username": sender.username if sender else "Desconocido",
            "receiver_id": h.receiver_id,
            "receiver_username": receiver.username if receiver else "Desconocido",
            "exchanged_on": h.exchanged_on
        })

    return enriched
