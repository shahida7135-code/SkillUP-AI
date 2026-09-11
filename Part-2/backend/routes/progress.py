from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.progress import Progress


router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)


@router.post("/update")
def update_progress(
    user_id: int,
    skill_id: int,
    progress_percentage: float,
    db: Session = Depends(get_db)
):
    # Check if progress already exists
    progress = db.query(Progress).filter(
        Progress.user_id == user_id,
        Progress.skill_id == skill_id
    ).first()

    # Keep percentage between 0 and 100
    progress_percentage = max(0, min(100, progress_percentage))

    if progress:
        progress.progress_percentage = progress_percentage
        progress.completed = progress_percentage >= 100
    else:
        progress = Progress(
            user_id=user_id,
            skill_id=skill_id,
            progress_percentage=progress_percentage,
            completed=progress_percentage >= 100
        )
        db.add(progress)

    db.commit()
    db.refresh(progress)

    return {
        "message": "Progress updated successfully",
        "user_id": progress.user_id,
        "skill_id": progress.skill_id,
        "progress_percentage": progress.progress_percentage,
        "completed": progress.completed
    }


@router.get("/{user_id}")
def get_progress(
    user_id: int,
    db: Session = Depends(get_db)
):
    progress = db.query(Progress).filter(
        Progress.user_id == user_id
    ).all()

    return progress