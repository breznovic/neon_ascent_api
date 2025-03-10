import random
from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from models import Weapon
from schemas import Weapon as WeaponSchema

router = APIRouter()


@router.get("/weapons/", response_model=List[WeaponSchema])
def get_weapons(db: Session = Depends(get_db)):
    weapons = db.query(Weapon).all()
    return weapons


@router.get("/weapons/random/", response_model=WeaponSchema)
def get_random_weapon(
    charisma: int = Query(..., description="Charisma of the character"),
    db: Session = Depends(get_db)
):
    weapons = db.query(Weapon).all()
    if not weapons:
        raise HTTPException(status_code=404, detail="No weapons found")

    weapon = random.choice(weapons)
    discounted_price = max(0, weapon.price - 2 * charisma)
    weapon.price = discounted_price
    return weapon
