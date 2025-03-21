from pydantic import BaseModel
from typing import List, Optional


class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str


class Config:
    from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class WeaponBase(BaseModel):
    name: str
    damage: int
    weapon_type: str
    price: int


class Weapon(WeaponBase):
    id: int

    class Config:
        orm_mode = True


class WeaponResponse(BaseModel):
    id: int
    name: str
    damage: int
    weapon_type: str
    price: int

    class Config:
        from_attributes = True

class BuyWeaponRequest(BaseModel):
    discounted_price: int


class CharacterCreate(BaseModel):
    name: str
    health: int = 100
    strength: int = 0
    intelligence: int = 0
    dexterity: int = 0
    charisma: int = 0
    experience: int = 0
    credits: int = 0
    has_completed_survey: Optional[bool] = False
    status: str = "Unemployed"
    weapon: Optional[WeaponResponse] = None
    level: int = 1


class CharacterResponse(BaseModel):
    id: int
    name: str
    health: int
    strength: int
    intelligence: int
    dexterity: int
    charisma: int
    experience: int
    credits: int
    has_completed_survey: Optional[bool] = None
    status: Optional[str] = None
    weapon: Optional[WeaponResponse] = None
    level: int

    class Config:
        from_attributes = True


class OptionModifiers(BaseModel):
    strength: int = 0
    intelligence: int = 0
    dexterity: int = 0
    charisma: int = 0
    credits: int = 0


class Option(BaseModel):
    text: str
    modifiers: OptionModifiers


class QuestionBase(BaseModel):
    text: str
    options: List[Option]


class QuestionCreate(QuestionBase):
    pass


class Question(QuestionBase):
    id: int

    class Config:
        from_attributes = True

class UpdateJobRequest(BaseModel):
    job: str