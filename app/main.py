from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .mock_data import mock_story_parts
from .routes import router as story_router
from .openai_utils import generate_choices

class Choice(BaseModel):
    choice: str
    prev_title: str
    prev_content: str

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
    first_part_key = "start"
    prompt = "魅力的な物語のタイトルと最初の段落を作成し、その後に続く物語の分岐を20文字以内程度の2つの選択肢として提供してください。返答は以下のようなフォーマットで返し、物語のタイトルを <Title> に、内容を <Content> に、選択肢1を <Choice 1> に、選択肢2を <Choice 2> に入れてください。決してコードは書かないでくださいね。"
    first_part = generate_choices(prompt, first_part_key)
    return first_part

@app.post("/api/story/next")
async def get_next_part(choice: Choice):
    if choice.choice:
        prompt = f"前回、あなたは、物語のタイトル: '{choice.prev_title}'\n物語の内容: '{choice.prev_content}'を作成しました。その後に続く物語を、\nユーザーが選択した選択肢: '{choice.choice}'\nこの情報に基づいて続きの物語の段落を作成してください。さらにその後に続く物語の分岐を20文字以内程度の2つの選択肢として提供してください。返答は以下のようなフォーマットで返し、物語のタイトルを <Title> に、内容を <Content> に、選択肢1を <Choice 1> に、選択肢2を <Choice 2> に入れてください。決してコードは書かないでくださいね。"
        next_part = generate_choices(prompt, choice.choice)
        return next_part
    else:
        raise HTTPException(status_code=422, detail="Invalid choice value")
