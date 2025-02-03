import google.generativeai as genai
from dotenv import load_dotenv
import os

# 取得したAPIキーを設定
load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)


# Gemini プロンプト
def generate_interview_questions(text, mode="自己PR"):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
  以下の文章は、面接での{mode}です。この内容に基づいて、面接官が聞きそうな質問をセリフとして1つ出力してください。

  【{mode}】
  "{text}"

  【想定質問】
  """
    response = model.generate_content(prompt)
    print(f"response: {response.text}")
    return response.text


if __name__ == "__main__":
    # 自己PRを入力
    user_input = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"

    # 質問生成
    questions = generate_interview_questions(user_input)
    print(questions)
