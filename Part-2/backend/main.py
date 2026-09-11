from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

# ============================================================
# Import all models
# ============================================================

from models.roadmap import (
    Department,
    Career,
    Skill,
    CareerSkill,
    Roadmap,
    RoadmapItem
)

from models.progress import Progress

from models.course import (
    Course,
    CourseResource
)

from models.quiz import (
    QuizQuestion,
    QuizAttempt
)


# ============================================================
# Create database tables
# ============================================================

Base.metadata.create_all(bind=engine)


# ============================================================
# FastAPI Application
# ============================================================

app = FastAPI(
    title="SkillBridge AI - Personalized Learning Roadmap",
    description=(
        "API for generating personalized learning roadmaps, "
        "managing learning fields and careers, tracking student "
        "progress, providing learning resources, and conducting quizzes."
    ),
    version="1.0.0"
)


# ============================================================
# CORS Configuration
# ============================================================
#
# Vite may run the frontend on port 5173 or 5174.
# Both ports are allowed here.
#
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# Import API Routes
# ============================================================

from routes.roadmap import router as roadmap_router
from routes.progress import router as progress_router
from routes.courses import router as courses_router
from routes.quiz import router as quiz_router


# ============================================================
# Register API Routes
# ============================================================

app.include_router(roadmap_router)
app.include_router(progress_router)
app.include_router(courses_router)
app.include_router(quiz_router)


# ============================================================
# Root Endpoint
# ============================================================

@app.get("/")
def home():
    return {
        "message": "SkillBridge AI Roadmap API is running!"
    }


# ============================================================
# Health Check Endpoint
# ============================================================

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected"
    }