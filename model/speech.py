from gtts import gTTS
from IPython.display import Audio
from pydub import AudioSegment
from question import first_question
import pygame


# 音声ファイルを作成
def create_mp3(text, filename):
    tts = gTTS(text, lang="ja")
    tts.save(filename)


# 音声ファイルを再生
def play_mp3(filename):
    # pygame を初期化
    pygame.mixer.init()

    # 音声ファイルをロードして再生
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    # 音声の再生が終わるまで待つ
    print("Playing...")
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


if __name__ == "__main__":
    text = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"
    question = first_question(text)
    create_mp3(question, "../audio/gTTS_test.mp3")
    play_mp3("../audio/gTTS_test.mp3")
