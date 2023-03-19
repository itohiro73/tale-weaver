from fastapi import FastAPI
from .mock_data import mock_story_parts
from .routes import router as story_router

app = FastAPI()

app.include_router(story_router)

@app.get("/api/story/first-part")
async def get_first_part():
    return mock_story_parts[0]
