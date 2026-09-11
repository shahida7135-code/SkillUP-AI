from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.roadmap import (
    Department,
    Career,
    CareerSkill,
    Roadmap,
    RoadmapItem
)

from schemas.roadmap import (
    RoadmapCreate,
    RoadmapResponse
)

from services.roadmap_service import generate_roadmap


router = APIRouter(
    prefix="/roadmap",
    tags=["Roadmap"]
)


# ============================================================
# GET ALL DEPARTMENTS / LEARNING FIELDS
# ============================================================

@router.get("/departments")
def get_departments(
    db: Session = Depends(get_db)
):

    departments = (
        db.query(Department)
        .order_by(Department.name)
        .all()
    )

    return [
        {
            "id": department.id,
            "name": department.name,
            "description": department.description
        }
        for department in departments
    ]


# ============================================================
# GET CAREERS / LEARNING PATHS FOR A DEPARTMENT
# ============================================================

@router.get("/departments/{department_id}/careers")
def get_department_careers(
    department_id: int,
    db: Session = Depends(get_db)
):

    department = db.query(Department).filter(
        Department.id == department_id
    ).first()

    if not department:

        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    careers = db.query(Career).filter(
        Career.department_id == department_id
    ).order_by(Career.name).all()

    return [
        {
            "id": career.id,
            "name": career.name,
            "department_id": career.department_id
        }
        for career in careers
    ]


# ============================================================
# GET SKILLS FOR A CAREER
# ============================================================

@router.get("/careers/{career_id}/skills")
def get_career_skills(
    career_id: int,
    db: Session = Depends(get_db)
):

    career = db.query(Career).filter(
        Career.id == career_id
    ).first()

    if not career:

        raise HTTPException(
            status_code=404,
            detail="Career not found"
        )

    career_skills = (
        db.query(CareerSkill)
        .filter(CareerSkill.career_id == career_id)
        .order_by(CareerSkill.order)
        .all()
    )

    return [
        {
            "skill_id": item.skill_id,
            "skill_name": item.skill.name,
            "priority": item.priority,
            "order": item.order,
            "estimated_weeks": item.estimated_weeks
        }
        for item in career_skills
    ]


# ============================================================
# GENERATE PERSONALIZED ROADMAP
# ============================================================

@router.post(
    "/generate",
    response_model=RoadmapResponse
)
def create_roadmap(
    data: RoadmapCreate,
    db: Session = Depends(get_db)
):

    roadmap = generate_roadmap(
        db=db,
        user_id=data.user_id,
        career_id=data.career_id
    )

    if not roadmap:

        raise HTTPException(
            status_code=404,
            detail="Career not found"
        )

    return roadmap