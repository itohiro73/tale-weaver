from fastapi import APIRouter

router = APIRouter()

@router.get("/api/story/first-part")
async def get_first_part():
    return {"message": "Hello, World!"}
