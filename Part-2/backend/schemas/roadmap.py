from pydantic import BaseModel
from typing import List, Optional


# Request from frontend
class RoadmapCreate(BaseModel):
    user_id: int
    career_id: int


# Skill returned in roadmap
class SkillResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        from_attributes = True


# Individual roadmap item
class RoadmapItemResponse(BaseModel):
    id: int
    skill_id: int
    order: int
    priority: str
    estimated_weeks: float
    skill: SkillResponse

    class Config:
        from_attributes = True


# Complete roadmap response
class RoadmapResponse(BaseModel):
    id: int
    user_id: int
    career_id: int
    items: List[RoadmapItemResponse]

    class Config:
        from_attributes = True