import sys
from pprint import pprint

sys.path.append("./")

from .chat import Chatbot
from .record import run_GUI, voice_filename
from .speech import create_mp3, play_mp3, idx
from .transcript import transcript


def app_run(user_input, directory, filename, mode="自己PR"):
    bot = Chatbot(mode)
    question = bot.first_question(user_input)
    dialogue = [("面接官", question)]

    while True:
        # 生成した質問の音声を再生
        path = f"{directory}/{filename}"
        create_mp3(question, path)
        play_mp3(path)

        run_GUI(directory)
        answer = transcript(directory, voice_filename)
        question = bot.next_question(answer)

        dialogue.append(("受験生", answer))
        dialogue.append(("面接官", question))
        pprint(dialogue)


if __name__ == "__main__":
    user_input = input("自己PRを入力してください：")
    directory = "../audio"
    filename = "question"
    app_run(user_input, directory, filename)
