from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .models import User, StudentProfile
from .schemas import ProfileIn, ProfileOut
from .dependencies import current_user

router = APIRouter(prefix="/api/profile", tags=["Student Profile"])

def profile_dict(profile, user):
    return {"user_id": user.id, "email": user.email, "full_name": profile.full_name, "phone": profile.phone,
            "branch": profile.branch, "education_level": profile.education_level, "college": profile.college,
            "graduation_year": profile.graduation_year, "target_career": profile.target_career, "bio": profile.bio}

@router.get("", response_model=ProfileOut)
def get_profile(user: User = Depends(current_user), db: Session = Depends(get_db)):
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == user.id).first()
    if not profile:
        profile = StudentProfile(user_id=user.id, full_name="", phone="", branch="", education_level="", college="", target_career="", bio="")
        db.add(profile); db.commit(); db.refresh(profile)
    return profile_dict(profile, user)

@router.put("", response_model=ProfileOut)
def update_profile(data: ProfileIn, user: User = Depends(current_user), db: Session = Depends(get_db)):
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == user.id).first()
    if not profile:
        profile = StudentProfile(user_id=user.id)
        db.add(profile)
    for key, value in data.model_dump().items():
        setattr(profile, key, value)
    db.commit(); db.refresh(profile)
    return profile_dict(profile, user)
