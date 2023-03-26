import openai
import os
from typing import List

openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key:
    print("OPENAI_API_KEY is set.")
else:
    print("OPENAI_API_KEY is not set.")

def generate_choices(prompt, title="", content="", is_conclusion=False):
    if is_conclusion:
        formatted_prompt = f"{prompt}\n\n"
    else:
        formatted_prompt = (
            f"{prompt}\n\n"
            f"タイトル: <Title>\n"
            f"内容: <Content>\n\n"
            f"選択肢1: <Choice 1>\n"
            f"選択肢2: <Choice 2>\n"
        )

    max_retries = 5
    retries = 0

    while retries < max_retries:
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
        parsed_response = parse_response(response.choices[0].text.strip())

        if is_valid_response(parsed_response):
            return parsed_response
        else:
            retries += 1

    # すべての再試行が失敗した場合は、エラーを返す
    raise ValueError("Failed to generate a valid response")

def is_valid_response(response: dict) -> bool:
    print("Validating response: ", response)
    base_conditions = [
        response["title"],
        response["content"],
   ]

    if "choices" in response and len(response["choices"]) >= 2:
        choice_conditions = [
            response["choices"][0],
            response["choices"][1]
        ]
    else:
        choice_conditions = []

    return all(base_conditions + choice_conditions)

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

    if len(choices) > 0:
        # Ensure at least two choices are extracted
        while len(choices) < 2:
            choices.append("")

        return {"title": title, "content": content, "choices": choices[:2]}
    else:
        return {"title": title, "content": content}
