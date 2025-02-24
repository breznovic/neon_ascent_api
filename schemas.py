from pydantic import BaseModel


class CharacterCreate(BaseModel):
    name: str
    health: int = 100
    strength: int = 1
    intelligence: int = 1
    dexterity: int = 1
    charisma: int = 1
    experience: int = 0
    credits: int = 0


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

    class Config:
        orm_mode = True
