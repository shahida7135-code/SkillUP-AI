from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# ============================================================
# DEPARTMENT / LEARNING FIELD
# ============================================================

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    careers = relationship(
        "Career",
        back_populates="department"
    )


# ============================================================
# CAREER / LEARNING PATH
# ============================================================

class Career(Base):
    __tablename__ = "careers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=True
    )

    department = relationship(
        "Department",
        back_populates="careers"
    )

    skills = relationship(
        "CareerSkill",
        back_populates="career",
        cascade="all, delete-orphan"
    )

    roadmaps = relationship(
        "Roadmap",
        back_populates="career"
    )


# ============================================================
# SKILL
# ============================================================

class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String,
        unique=True,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    career_links = relationship(
        "CareerSkill",
        back_populates="skill"
    )

    roadmap_items = relationship(
        "RoadmapItem",
        back_populates="skill"
    )


# ============================================================
# CAREER → SKILL
# ============================================================

class CareerSkill(Base):
    __tablename__ = "career_skills"

    id = Column(Integer, primary_key=True, index=True)

    career_id = Column(
        Integer,
        ForeignKey("careers.id"),
        nullable=False
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        nullable=False
    )

    priority = Column(
        String,
        default="Medium"
    )

    order = Column(
        Integer,
        nullable=False
    )

    estimated_weeks = Column(
        Float,
        default=1
    )

    career = relationship(
        "Career",
        back_populates="skills"
    )

    skill = relationship(
        "Skill",
        back_populates="career_links"
    )


# ============================================================
# ROADMAP
# ============================================================

class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        nullable=False
    )

    career_id = Column(
        Integer,
        ForeignKey("careers.id"),
        nullable=False
    )

    career = relationship(
        "Career",
        back_populates="roadmaps"
    )

    items = relationship(
        "RoadmapItem",
        back_populates="roadmap",
        cascade="all, delete-orphan"
    )


# ============================================================
# ROADMAP ITEM
# ============================================================

class RoadmapItem(Base):
    __tablename__ = "roadmap_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    roadmap_id = Column(
        Integer,
        ForeignKey("roadmaps.id"),
        nullable=False
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        nullable=False
    )

    order = Column(
        Integer,
        nullable=False
    )

    priority = Column(
        String,
        default="Medium"
    )

    estimated_weeks = Column(
        Float,
        default=1
    )

    roadmap = relationship(
        "Roadmap",
        back_populates="items"
    )

    skill = relationship(
        "Skill",
        back_populates="roadmap_items"
    )