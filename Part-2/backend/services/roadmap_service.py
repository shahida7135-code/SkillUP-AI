from sqlalchemy.orm import Session

from models.roadmap import Career, CareerSkill, Roadmap, RoadmapItem


def generate_roadmap(
    db: Session,
    user_id: int,
    career_id: int
):
    # Find the selected career
    career = db.query(Career).filter(
        Career.id == career_id
    ).first()

    if not career:
        return None

    # Create a new roadmap
    roadmap = Roadmap(
        user_id=user_id,
        career_id=career_id
    )

    db.add(roadmap)
    db.commit()
    db.refresh(roadmap)

    # Get skills for this career in learning order
    career_skills = (
        db.query(CareerSkill)
        .filter(CareerSkill.career_id == career_id)
        .order_by(CareerSkill.order)
        .all()
    )

    # Add each skill to the roadmap
    for career_skill in career_skills:

        roadmap_item = RoadmapItem(
            roadmap_id=roadmap.id,
            skill_id=career_skill.skill_id,
            order=career_skill.order,
            priority=career_skill.priority,
            estimated_weeks=career_skill.estimated_weeks
        )

        db.add(roadmap_item)

    db.commit()
    db.refresh(roadmap)

    return roadmap