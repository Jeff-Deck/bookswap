from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
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


