from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.quiz import QuizQuestion, QuizAttempt
from models.progress import Progress


router = APIRouter(
    prefix="/quiz",
    tags=["Quiz"]
)


@router.get("/skill/{skill_id}")
def get_quiz_questions(
    skill_id: int,
    db: Session = Depends(get_db)
):
    questions = (
        db.query(QuizQuestion)
        .filter(QuizQuestion.skill_id == skill_id)
        .order_by(QuizQuestion.id)
        .all()
    )

    if not questions:
        raise HTTPException(
            status_code=404,
            detail="Quiz not available for this skill yet."
        )

    return [
        {
            "id": question.id,
            "skill_id": question.skill_id,
            "question": question.question,
            "options": [
                question.option_a,
                question.option_b,
                question.option_c,
                question.option_d
            ]
        }
        for question in questions
    ]


@router.post("/submit")
def submit_quiz(
    user_id: int,
    skill_id: int,
    answers: dict,
    db: Session = Depends(get_db)
):
    questions = (
        db.query(QuizQuestion)
        .filter(QuizQuestion.skill_id == skill_id)
        .order_by(QuizQuestion.id)
        .all()
    )

    if not questions:
        raise HTTPException(
            status_code=404,
            detail="Quiz not available for this skill yet."
        )

    score = 0

    for question in questions:
        user_answer = answers.get(str(question.id))

        if user_answer == question.correct_answer:
            score += 1

    total_questions = len(questions)

    percentage = round(
        (score / total_questions) * 100
    )

    passed = percentage >= 60

    attempt = QuizAttempt(
        user_id=user_id,
        skill_id=skill_id,
        score=score,
        total_questions=total_questions,
        passed=1 if passed else 0
    )

    db.add(attempt)

    if passed:
        progress = (
            db.query(Progress)
            .filter(
                Progress.user_id == user_id,
                Progress.skill_id == skill_id
            )
            .first()
        )

        if progress:
            progress.progress_percentage = 100
            progress.completed = True
        else:
            progress = Progress(
                user_id=user_id,
                skill_id=skill_id,
                progress_percentage=100,
                completed=True
            )
            db.add(progress)

    db.commit()
    db.refresh(attempt)

    return {
        "message": (
            "Quiz passed successfully!"
            if passed
            else "Quiz not passed. Please try again."
        ),
        "user_id": user_id,
        "skill_id": skill_id,
        "score": score,
        "total_questions": total_questions,
        "percentage": percentage,
        "passed": passed
    }


@router.get("/attempts/{user_id}")
def get_quiz_attempts(
    user_id: int,
    db: Session = Depends(get_db)
):
    attempts = (
        db.query(QuizAttempt)
        .filter(QuizAttempt.user_id == user_id)
        .order_by(QuizAttempt.id.desc())
        .all()
    )

    return attempts