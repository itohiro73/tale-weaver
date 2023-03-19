from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .mock_data import mock_story_parts
from .routes import router as story_router

class Choice(BaseModel):
    choice: str

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(story_router)

@app.get("/api/story/first")
async def get_first_part():
    return mock_story_parts["start"]

@app.post("/api/story/next")
async def get_next_part(choice: Choice):
    if choice.choice in mock_story_parts.keys():
        return mock_story_parts[choice.choice]
    else:
        raise HTTPException(status_code=422, detail="Invalid choice value")
