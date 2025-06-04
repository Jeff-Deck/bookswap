from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from api.database import get_db
from api.ratings import crud, schemas
from api import models


router = APIRouter(prefix="/ratings", tags=["Ratings"])

@router.post("/", response_model=schemas.ExchangeRatingResponse)
def create_rating(
    rating_data: schemas.ExchangeRatingCreate,
    db: Session = Depends(get_db)
):
    return crud.create_rating(db, rating_data)  # ⬅️ ya no usamos user fijo


@router.get("/user/{user_id}", response_model=list[schemas.ExchangeRatingResponse])
def get_user_ratings(user_id: int, db: Session = Depends(get_db)):
    return crud.get_ratings_for_user(db, user_id)

@router.get("/by-rater/{rater_id}", response_model=list[schemas.ExchangeRatingResponse])
def get_ratings_by_rater(rater_id: int, db: Session = Depends(get_db)):
    return db.query(models.ExchangeRating).filter(models.ExchangeRating.rater_id == rater_id).all()

@router.get("/top5")
def get_top_5_users_by_rating(db: Session = Depends(get_db)):
    results = (
        db.query(
            models.ExchangeRating.rated_user_id,
            func.avg(models.ExchangeRating.score).label("avg_score"),
            func.count(models.ExchangeRating.id).label("count")
        )
        .group_by(models.ExchangeRating.rated_user_id)
        .having(func.count(models.ExchangeRating.id) >= 1)
        .order_by(func.avg(models.ExchangeRating.score).desc())
        .limit(5)
        .all()
    )

    response = []
    for user_id, avg_score, count in results:
        user = db.query(models.CustomUser).filter(models.CustomUser.id == user_id).first()
        if user:
            response.append({
                "id": user.id,
                "username": user.username,
                "average": round(avg_score, 2),
                "count": count
            })
    return response
