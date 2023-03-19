from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .mock_data import mock_story_parts
from .routes import router as story_router

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

@app.get("/api/story/first-part")
async def get_first_part():
    return mock_story_parts[0]
