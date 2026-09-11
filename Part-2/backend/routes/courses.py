from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.course import Course


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


# ==========================================
# GET ALL COURSES
# ==========================================

@router.get("/")
def get_courses(
    db: Session = Depends(get_db)
):
    courses = (
        db.query(Course)
        .order_by(
            Course.department,
            Course.title
        )
        .all()
    )

    return courses


# ==========================================
# GET COURSES BY DEPARTMENT
# ==========================================

@router.get("/department/{department}")
def get_courses_by_department(
    department: str,
    db: Session = Depends(get_db)
):
    courses = (
        db.query(Course)
        .filter(
            Course.department.ilike(department)
        )
        .order_by(Course.title)
        .all()
    )

    return courses


# ==========================================
# GET COURSES BY SKILL
# ==========================================

@router.get("/skill/{skill}")
def get_courses_by_skill(
    skill: str,
    db: Session = Depends(get_db)
):
    courses = (
        db.query(Course)
        .filter(
            Course.skill.ilike(skill)
        )
        .order_by(Course.title)
        .all()
    )

    return courses


# ==========================================
# GET COURSES BY LEVEL
# ==========================================

@router.get("/level/{level}")
def get_courses_by_level(
    level: str,
    db: Session = Depends(get_db)
):
    courses = (
        db.query(Course)
        .filter(
            Course.level.ilike(level)
        )
        .order_by(Course.title)
        .all()
    )

    return courses


# ==========================================
# SEARCH COURSES
# ==========================================

@router.get("/search/{query}")
def search_courses(
    query: str,
    db: Session = Depends(get_db)
):
    search_text = f"%{query}%"

    courses = (
        db.query(Course)
        .filter(
            (Course.title.ilike(search_text))
            | (Course.skill.ilike(search_text))
            | (Course.category.ilike(search_text))
            | (Course.department.ilike(search_text))
        )
        .order_by(Course.title)
        .all()
    )

    return courses


# ==========================================
# GET COURSE BY ID
# ==========================================

@router.get("/{course_id}")
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course = (
        db.query(Course)
        .filter(
            Course.id == course_id
        )
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course