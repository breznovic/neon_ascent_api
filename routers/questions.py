from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from database import SessionLocal
from models import Question
from schemas import Question as QuestionSchema
from typing import List


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/questions/", response_model=List[QuestionSchema])
def get_questions(db: Session = Depends(get_db)):
    return db.query(Question).order_by(func.random()).limit(3).all()



