from fastapi import APIRouter, HTTPException
from services.youtube_service import search_youtube_videos

router = APIRouter(
    prefix="/api/youtube",
    tags=["youtube"]
)

@router.get("/search")
def get_youtube_resources(query: str, max_results: int = 10):
    results = search_youtube_videos(query, max_results)
    if isinstance(results, dict) and "error" in results:
        raise HTTPException(status_code=500, detail=results["error"])
    return {"videos": results}