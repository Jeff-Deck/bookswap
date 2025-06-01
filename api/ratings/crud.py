from sqlalchemy.orm import Session
from api.ratings import models, schemas

def create_rating(db: Session, rating_data: schemas.ExchangeRatingCreate):
    db_rating = models.ExchangeRating(
        exchange_id=rating_data.exchange_id,
        rated_user_id=rating_data.rated_user_id,
        rater_id=rating_data.rater_id,  # ⬅️ usar el que viene del frontend
        score=rating_data.score,
        comment=rating_data.comment,
    )
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating


def get_ratings_for_user(db: Session, user_id: int):
    return db.query(models.ExchangeRating).filter(models.ExchangeRating.rated_user_id == user_id).all()
