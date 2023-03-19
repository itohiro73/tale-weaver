from fastapi import APIRouter

router = APIRouter()

@router.get("/stories/")
async def get_stories():
    return [{"id": 1, "title": "Sample Story"}]

