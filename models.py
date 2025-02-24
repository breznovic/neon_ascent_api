from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)


class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, ForeignKey("users.username"))
    user_id = Column(Integer, ForeignKey("users.id"))
    health = Column(Integer, default=100)
    strength = Column(Integer, default=1)
    intelligence = Column(Integer, default=1)
    dexterity = Column(Integer, default=1)
    charisma = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    credits = Column(Integer, default=0)
