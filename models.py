from sqlalchemy import JSON, Boolean, Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    characters = relationship("Character", back_populates="user")


class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    health = Column(Integer, default=100)
    strength = Column(Integer, default=0)
    intelligence = Column(Integer, default=0)
    dexterity = Column(Integer, default=0)
    charisma = Column(Integer, default=0)
    experience = Column(Integer, default=0)
    credits = Column(Integer, default=0)
    has_completed_survey = Column(Boolean, default=False)
    status = Column(String, default="Unemployed")
    weapon_id = Column(Integer, ForeignKey("weapons.id"), nullable=True)
    level = Column(Integer, default=1)

    user = relationship("User", back_populates="characters")
    weapon = relationship("Weapon")


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    options = Column(JSON)


class Weapon(Base):
    __tablename__ = "weapons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    damage = Column(Integer)
    weapon_type = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"<Weapon(name={self.name}, damage={self.damage}, type={self.weapon_type}, price={self.price})>"
