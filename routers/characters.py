from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from schemas import CharacterCreate, CharacterResponse, BuyWeaponRequest, UpdateJobRequest
from models import Character, User, Weapon
from database import SessionLocal
from .auth import get_current_user

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/characters/")
def get_characters():
    return {"message": "List of characters"}


@router.post("/characters/", response_model=CharacterResponse)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    db_character = Character(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character


@router.post("/characters/update-attributes-after-survey/")
def update_character_attributes(
    attributes: dict,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    character = db.query(Character).filter(
        Character.user_id == current_user.id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    for attr, value in attributes.items():
        setattr(character, attr, getattr(character, attr) + value)

    character.credits += 10

    character.has_completed_survey = True

    db.commit()
    db.refresh(character)
    return character


@router.get("/characters/me", response_model=CharacterResponse)
def get_character_me(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    character = db.query(Character).filter(
        Character.user_id == current_user.id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character


@router.post("/characters/{character_id}/buy-weapon/{weapon_id}", response_model=CharacterResponse)
def buy_weapon(
    character_id: int,
    weapon_id: int,
    request: BuyWeaponRequest,
    db: Session = Depends(get_db),
):
    discounted_price = request.discounted_price

    character = db.query(Character).filter(
        Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    weapon = db.query(Weapon).filter(Weapon.id == weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")

    if character.weapon_id:
        current_weapon = db.query(Weapon).filter(
            Weapon.id == character.weapon_id).first()
        if current_weapon:
            sell_price = current_weapon.price // 2
            character.credits += sell_price

    if character.credits < discounted_price:
        raise HTTPException(status_code=400, detail="Not enough credits")

    character.weapon_id = weapon_id
    character.credits -= discounted_price

    db.commit()
    db.refresh(character)

    return character


@router.post("/characters/{character_id}/sell-weapon/", response_model=CharacterResponse)
def sell_weapon(
    character_id: int,
    db: Session = Depends(get_db),
):
    character = db.query(Character).filter(
        Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    if not character.weapon_id:
        raise HTTPException(status_code=400, detail="No weapon to sell")

    weapon = db.query(Weapon).filter(Weapon.id == character.weapon_id).first()
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")

    sell_price = weapon.price // 2
    character.credits += sell_price
    character.weapon_id = None

    db.commit()
    db.refresh(character)

    return character


@router.post("/characters/{character_id}/update-job/", response_model=CharacterResponse)
def update_job(
    character_id: int,
    request: UpdateJobRequest,
    db: Session = Depends(get_db),
):
    character = db.query(Character).filter(
        Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")

    character.status = request.job
    db.commit()
    db.refresh(character)

    return character
