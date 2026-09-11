from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from ..database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(320), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class StudentProfile(Base):
    __tablename__ = "student_profiles"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True, nullable=False)
    full_name = Column(String(120), default="", nullable=False)
    phone = Column(String(30), default="", nullable=False)
    branch = Column(String(120), default="", nullable=False)
    education_level = Column(String(80), default="", nullable=False)
    college = Column(String(180), default="", nullable=False)
    graduation_year = Column(Integer, nullable=True)
    target_career = Column(String(160), default="", nullable=False)
    bio = Column(String(1000), default="", nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
