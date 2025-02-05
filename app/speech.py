from gtts import gTTS
from IPython.display import Audio
from pydub import AudioSegment
import pygame, os

try:
    from .chat import Chatbot
except:
    from chat import Chatbot

global idx
idx = 0


# 音声ファイルを作成
def create_mp3(text, filename):
    global idx
    idx += 1

    path = f"{filename}{idx}.mp3"
    tts = gTTS(text, lang="ja")
    tts.save(path)


# 音声ファイルを再生
def play_mp3(filename):
    # pygame を初期化
    pygame.mixer.init()

    # 音声ファイルをロードして再生
    pygame.mixer.music.load(f"{filename}{idx}.mp3")
    pygame.mixer.music.play()

    # 音声の再生が終わるまで待つ
    print("Playing...")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    text = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"
    bot = Chatbot()
    question = bot.first_question(text)
    filename = "../audio/gTTS_test"
    create_mp3(question, filename)
    play_mp3(filename)
