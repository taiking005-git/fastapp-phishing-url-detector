from turtle import title
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from database import Base
from schema import Roles
# from pydantic import BaseModel


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(Roles), default="user")
    isActive = Column(Boolean, default=False)

    reports = relationship("Report", back_populates="user")



class Report(Base):
    __tablename__ = "report"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    site_url = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    isPhishing = Column(Boolean, default=False)

    user = relationship("User", back_populates="reports")


