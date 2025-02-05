import sys

sys.path.append("./")

from .chat import Chatbot
from .record import run_GUI, voice_filename
from .speech import create_mp3, play_mp3, idx
from .transcript import transcript


def app_run(user_input, directory, filename, mode="自己PR"):
    bot = Chatbot(mode)
    question = bot.first_question(user_input)

    while True:
        # 生成した質問の音声を再生
        path = f"{directory}/{filename}"
        create_mp3(question, f"{path}{idx}")
        play_mp3(f"{path}{idx}")

        run_GUI(directory)
        answer = transcript(directory, voice_filename)
        question = bot.next_question(answer)


if __name__ == "__main__":
    user_input = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"
    directory = "../audio"
    filename = "question"
    app_run(user_input, directory, filename)
