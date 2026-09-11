from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)

    department = Column(String, nullable=False)
    category = Column(String, nullable=True)
    skill = Column(String, nullable=False)

    level = Column(String, default="Beginner")

    provider = Column(String, nullable=False)
    duration = Column(String, nullable=True)

    url = Column(String, nullable=False)

    resources = relationship(
        "CourseResource",
        back_populates="course",
        cascade="all, delete-orphan"
    )


class CourseResource(Base):
    __tablename__ = "course_resources"

    id = Column(Integer, primary_key=True, index=True)

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        nullable=False
    )

    title = Column(String, nullable=False)
    resource_type = Column(String, default="Tutorial")
    url = Column(String, nullable=False)

    course = relationship(
        "Course",
        back_populates="resources"
    )