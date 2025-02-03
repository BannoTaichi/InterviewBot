from gtts import gTTS
from IPython.display import Audio
from pydub import AudioSegment
from create_sentence import generate_interview_questions

text = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"
question = generate_interview_questions(text)
tts = gTTS(question, lang="ja")
tts.save("gTTS_test.mp3")

# 音声ファイルを読み込み
sound = AudioSegment.from_file("gTTS_test.mp3")

# 速度を 1.5 倍（速くする）
speed_up = sound.speedup(playback_speed=1.3, chunk_size=70)
speed_up.export("gTTS_fast.mp3", format="mp3")

Audio("gTTS_fast.mp3", autoplay=True)
