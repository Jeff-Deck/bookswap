from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from api.database import Base

class ExchangeRating(Base):
    __tablename__ = "exchange_ratings"

    id = Column(Integer, primary_key=True, index=True)
    exchange_id = Column(Integer)
    rater_id = Column(Integer)
    rated_user_id = Column(Integer)
    score = Column(Integer)
    comment = Column(Text, nullable=True)
    rated_at = Column(DateTime, default=datetime.utcnow)
