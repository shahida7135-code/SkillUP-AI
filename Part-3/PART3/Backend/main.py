from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.youtube import router as youtube_router

app = FastAPI(title="SkillBridge API - Part 3")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(youtube_router)

@app.get("/")
def read_root():
    return {"message": "SkillBridge API is running. Ready for team merge."}