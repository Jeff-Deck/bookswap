from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ExchangeRatingCreate(BaseModel):
    exchange_id: int
    rated_user_id: int
    rater_id: int  # ⬅️ nuevo campo
    score: int
    comment: Optional[str] = None

class ExchangeRatingResponse(BaseModel):
    id: int
    exchange_id: int
    rater_id: int
    rated_user_id: int
    score: int
    comment: Optional[str]
    rated_at: datetime

    class Config:
        orm_mode = True
