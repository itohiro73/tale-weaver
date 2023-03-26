import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
if openai.api_key:
    print("OPENAI_API_KEY is set.")
else:
    print("OPENAI_API_KEY is not set.")

def test_prompt(prompt):
    print("Sending prompt: ", prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
    )
    print("Received response:", response.choices[0].text.strip())

if __name__ == "__main__":
    # テスト用のプロンプトを作成

    # 物語の続き用プロンプト
    # prev_title = "悲しい宝石"
    # prev_content = "彼は石を拾ってみた。石は美しく輝いていて、どんな宝石かを想像すると驚くほどの美しさだった。彼は石を抱え、島を出ることを決めた。しかし、彼が島を去ると、宝石から悲しい泣き声が聞こえてきた。"
    # choice = "石を残す"
    # prompt = (
    #     f"前回、あなたは、物語のタイトル: '{prev_title}'\n物語の内容: '{prev_content}'を作成しました。その後に続く物語を、\nユーザーが選択した選択肢: '{choice}'\nこの情報に基づいて続きの物語の段落を作成してください。さらにその後に続く物語の分岐を20文字以内程度の2つの選択肢として提供してください。返答は以下のようなフォーマットで返し、物語のタイトルを <Title> に、内容を <Content> に、選択肢1を <Choice 1> に、選択肢2を <Choice 2> に入れてください。決してコードは書かないでくださいね。\n\n"
    #     f"タイトル: <Title>\n"
    #     f"内容: <Content>\n\n"
    #     f"選択肢1: <Choice 1>\n"
    #     f"選択肢2: <Choice 2>\n"
    # )

    # 物語の完結用プロンプト
    prev_title = "悲しい宝石"
    prev_content = "彼は悲しそうな宝石を抱きしめたまま、島から出ようとした。しかし、彼はどうしてもその宝石を捨てられなかった。彼は、宝石を島に残し、悲しそうに立ち去ろうと決心した。"
    choice = "島を去る"
    prompt = (
        f"前回、あなたは、物語のタイトル: '{prev_title}'\n物語の内容: '{prev_content}'を作成しました。その後に続く物語を、\nユーザーが選択した選択肢: '{choice}'\nこの情報に基づいて続きの物語の段落を作成してください。今回の段落で物語が完結するようにしてください。返答は以下のようなフォーマットで返し、物語のタイトルを <Title> に、内容を <Content> に入れてください。決してコードは書かないでくださいね。\n\nTitle: <Title>\nContent: <Content>\n"
    )

    # プロンプトをテスト
    test_prompt(prompt)
