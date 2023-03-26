import openai
import os
from typing import List

openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key:
    print("OPENAI_API_KEY is set.")
else:
    print("OPENAI_API_KEY is not set.")

def generate_choices(prompt, title="", content=""):
    formatted_prompt = (
        f"{prompt}\n\n"
        f"タイトル: <Title>\n"
        f"内容: <Content>\n\n"
        f"選択肢1: <Choice 1>\n"
        f"選択肢2: <Choice 2>\n"
    )
    print("Sending prompt:", formatted_prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=formatted_prompt,
        max_tokens=1024,
        n=1,
        stop=["タイトル:", "内容:", "選択肢1:", "選択肢2:"],
        temperature=0.7,
    )
    print("Received response:", response.choices[0].text.strip())
    return parse_response(response.choices[0].text.strip())

def parse_response(response_text):
    response_parts = response_text.split("\n")
    title = ""
    content = ""
    choices = []

    for part in response_parts:
        if part.startswith("タイトル:") or part.startswith("Title:"):
            title = part[len("タイトル:"):] if part.startswith("タイトル:") else part[len("Title:"):]
            title = title.strip()
        elif part.startswith("内容:") or part.startswith("Content:"):
            content = part[len("内容:"):] if part.startswith("内容:") else part[len("Content:"):]
            content = content.strip()
        elif part.startswith("選択肢1:") or part.startswith("Choice 1:"):
            choice = part[len("選択肢1:"):] if part.startswith("選択肢1:") else part[len("Choice 1:"):]
            choices.append(choice.strip())
        elif part.startswith("選択肢2:") or part.startswith("Choice 2:"):
            choice = part[len("選択肢2:"):] if part.startswith("選択肢2:") else part[len("Choice 2:"):]
            choices.append(choice.strip())

    # Ensure at least two choices are extracted
    while len(choices) < 2:
        choices.append("")

    return {"title": title, "content": content, "choices": choices[:2]}