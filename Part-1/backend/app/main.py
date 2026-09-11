import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .auth import models as auth_models
from .auth.routes import router as auth_router
from .auth.profile_routes import router as profile_router

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Skill Up AI API", version="1.0.0")
origins = [x.strip() for x in os.getenv("FRONTEND_ORIGIN", "http://localhost:5173,http://127.0.0.1:5173").split(",")]
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(profile_router)

@app.get("/")
def root():
    return {"service": "Skill Up AI", "module": "Part 1 - Authentication & Student Profile"}

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "Skill Up AI", "module": "part1"}
