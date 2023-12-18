from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from database import Base
from schema import Roles



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(Roles), default="user")
    isActive = Column(Boolean, default=False)

    # reports = relationship("Report", back_populates="user")


class Report(Base):
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    site_url = Column(String, nullable=False, unique=True)
    isPhishing = Column(String)


    # user = relationship("User", back_populates="reports")


