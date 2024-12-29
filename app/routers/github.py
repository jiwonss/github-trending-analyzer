from fastapi import APIRouter, HTTPException
from app.core.github import fetch_repositories

router = APIRouter(prefix="/github")


@router.get("/repositories")
async def get_repositories(stars: int = 100, topic: str = "python", page: int = 1):
    try:
        query = f"stars:>={stars} topic:{topic}"
        data = fetch_repositories(
            query=query, sort="stars", order="desc", per_page=100, page=page
        )
        return {"repositories": data.get("items", [])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
