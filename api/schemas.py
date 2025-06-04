from pydantic import BaseModel
from datetime import datetime

class ExchangeHistoryOut(BaseModel):
    id: int
    book_id: int
    sender_id: int
    sender_username: str
    receiver_id: int
    receiver_username: str
    exchanged_on: datetime

    class Config:
        orm_mode = True
