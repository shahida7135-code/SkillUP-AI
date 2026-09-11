from sqlalchemy import Column, Integer, Float, Boolean, ForeignKey

from database import Base


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)

    progress_percentage = Column(Float, default=0)
    completed = Column(Boolean, default=False)