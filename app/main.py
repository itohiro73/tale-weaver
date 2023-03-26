from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .mock_data import mock_story_parts
from .routes import router as story_router
from .openai_utils import generate_choices
import logging
import random

# ロガーの設定
logging.basicConfig(level=logging.DEBUG)

class Choice(BaseModel):
    choice: str
    prev_title: str
    prev_content: str
    choice_count: int

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://127.0.0.1",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
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
    logging.debug(f"received story/first request:")  # リクエストデータをログに出力
    first_part_key = "start"
    prompt = "魅力的な物語のタイトルと最初の段落を作成し、その後に続く物語の分岐を20文字以内程度の2つの選択肢として提供してください。返答は以下のようなフォーマットで返し、物語のタイトルを <Title> に、内容を <Content> に、選択肢1を <Choice 1> に、選択肢2を <Choice 2> に入れてください。決してコードは書かないでくださいね。"
    first_part = generate_choices(prompt, first_part_key)
    return first_part

@app.post("/api/story/next")
async def get_next_part(choice: Choice):
    logging.debug(f"choice: {choice}")  # リクエストデータをログに出力

    if choice.choice:
        # 選択肢のカウントが閾値に達しているか、確率的に完結する選択肢を生成する条件を満たすかを判断する
        is_conclusion_reached = choice.choice_count >= 5
        is_conclusion_probability_met = choice.choice_count > 3 and random.random() < 0.25 if choice.choice_count <= 4 else random.random() < 0.5

        # 完結条件に応じてプロンプトを変更
        if is_conclusion_reached or is_conclusion_probability_met:
            prompt = f"前回、あなたは、物語のタイトル: '{choice.prev_title}'\n物語の内容: '{choice.prev_content}'を作成しました。その後に続く物語を、\nユーザーが選択した選択肢: '{choice.choice}'\nこの情報に基づいて続きの物語の段落を作成してください。今回の段落で物語が完結するようにしてください。返答は以下のようなフォーマットで返し、物語のタイトルを <Title> に、内容を <Content> に入れてください。決してコードは書かないでくださいね。"
        else:
            prompt = f"前回、あなたは、物語のタイトル: '{choice.prev_title}'\n物語の内容: '{choice.prev_content}'を作成しました。その後に続く物語を、\nユーザーが選択した選択肢: '{choice.choice}'\nこの情報に基づいて続きの物語の段落を作成してください。さらにその後に続く物語の分岐を20文字以内程度の2つの選択肢として提供してください。返答は以下のようなフォーマットで返し、物語のタイトルを <Title> に、内容を <Content> に、選択肢1を <Choice 1> に、選択肢2を <Choice 2> に入れてください。決してコードは書かないでくださいね。"

        next_part = generate_choices(prompt, choice.choice)
        logging.debug(f"choice: {choice}")  # リクエストデータをログに出力
        return next_part
    else:
        raise HTTPException(status_code=422, detail="Invalid choice value")
