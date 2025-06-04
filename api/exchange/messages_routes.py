from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api import models
from datetime import datetime

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.get("/{exchange_request_id}")
def get_messages(exchange_request_id: int, db: Session = Depends(get_db)):
    messages = db.query(models.Message).filter(
        models.Message.exchange_request_id == exchange_request_id
    ).order_by(models.Message.timestamp).all()

    return [{
        "id": m.id,
        "sender_id": m.sender_id,
        "content": m.content,
        "timestamp": m.timestamp
    } for m in messages]

@router.post("/")
def post_message(data: dict, db: Session = Depends(get_db)):
    message = models.Message(
        exchange_request_id=data["exchange_request_id"],
        sender_id=data["sender_id"],
        content=data["content"]
    )
    db.add(message)
    db.commit()
    db.refresh(message)
    return {"status": "ok", "id": message.id}
