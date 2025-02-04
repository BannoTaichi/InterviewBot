import google.generativeai as genai
from dotenv import load_dotenv
import os

# 取得したAPIキーを設定
load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)


# Gemini プロンプト
def first_question(text, mode="自己PR"):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"""
  以下の文章は、面接での{mode}です。この内容に基づいて、面接官が聞きそうな質問をセリフとして1つ出力してください。
  なお読みが難しい漢字は平仮名で出力してください。

  【{mode}】
  "{text}"

  【想定質問】
  """
    response = model.generate_content(prompt)
    print(f"response: {response.text}")
    return response.text


if __name__ == "__main__":

    user_input = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"

    # 質問生成
    question = first_question(user_input)

    user_input = "はい、具体的には装置の銀の容量を増やし、膜厚条件を広げることで適切な膜厚条件を評価することができました。"

    # 質問生成
    question = first_question(user_input)
