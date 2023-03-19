from fastapi import FastAPI
from .routes import router as story_router

app = FastAPI()

app.include_router(story_router)

