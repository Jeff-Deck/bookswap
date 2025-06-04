from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api import models

router = APIRouter(prefix="/exchange-requests", tags=["Exchange Requests"])

@router.get("/received/{user_id}")
def get_received_requests(user_id: int, db: Session = Depends(get_db)):
    requests = db.query(models.ExchangeRequest).filter(
        models.ExchangeRequest.receiver_id == user_id
    ).all()

    results = []
    for req in requests:
        sender = db.query(models.CustomUser).filter(models.CustomUser.id == req.sender_id).first()
        book = db.query(models.Book).filter(models.Book.id == req.book_id).first()
        results.append({
            "id": req.id,
            "status": req.status,
            "timestamp": req.timestamp,
            "book_id": req.book_id,
            "book_title": book.title if book else "Desconocido",
            "sender_id": req.sender_id,
            "receiver_id": req.receiver_id,
            "sender_username": sender.username if sender else "Desconocido"
        })

    return results
