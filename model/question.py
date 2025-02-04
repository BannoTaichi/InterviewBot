import google.generativeai as genai
from dotenv import load_dotenv
import os

# 取得したAPIキーを設定
load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)


class Chatbot:
    # コンストラクタ
    def __init__(self, mode="自己PR"):
        self.mode = mode
        self.context = ""
        self.model = genai.GenerativeModel("gemini-pro")

    # 質問生成
    def first_question(self, text, mode="自己PR"):
        prompt = f"""
        以下の文章は、面接での{mode}とこれまでの面接内容です。この内容に基づいて、面接官が聞きそうな質問をセリフとして1つ出力してください。
        
        【出力のルール】
        なお読みが難しい漢字は平仮名で出力してください。
        前と同じような質問になりそうなら、適宜内容を変えてください。
        質問については、「行動を行なった理由」「論理的に正しいかどうか」「仕事における再現性があるか」などを重要な観点として考えてください。

        【{mode}】
        {text}

        【面接内容】
        面接官："""
        response = self.model.generate_content(prompt)
        self.context = prompt + response.text
        print(f"\nresponse: {response.text}")
        print(f"context: {self.context}\n")
        return response.text

    def next_question(self, text):
        prompt = f"""{self.context}
        受験生：{text}
        面接官："""
        response = self.model.generate_content(prompt)
        self.context = prompt + response.text
        print(f"response: {response.text}")
        print(f"context: {self.context}\n")
        return response.text


if __name__ == "__main__":
    user_input = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"
    bot = Chatbot()
    question = bot.first_question(user_input)

    while True:
        user_input = input("回答：")
        question = bot.next_question(user_input)
