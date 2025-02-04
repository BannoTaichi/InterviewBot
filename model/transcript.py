import speech_recognition as sr
from pydub import AudioSegment

# 音声認識オブジェクトを作成
recognizer = sr.Recognizer()


def transcript(audio_file):
    if audio_file.endswith(".mp3"):
        # MP3 を WAV に変換
        sound = AudioSegment.from_mp3(audio_file)
        sound.export("../audio/converted.wav", format="wav")
        audio_file = "../audio/converted.wav"

        print("MP3 を WAV に変換しました！")

    with sr.AudioFile(audio_file) as source:
        print("音声を認識中...")
        audio_data = recognizer.record(source)  # 音声データを取得

    # GoogleのSpeech-to-Text APIで文字起こし（日本語対応）
    try:
        text = recognizer.recognize_google(audio_data, language="ja-JP")  # 日本語
        print("認識結果:", text)
    except sr.UnknownValueError:
        print("音声を認識できませんでした")
    except sr.RequestError:
        print("Google Speech API に接続できませんでした")


if __name__ == "__main__":
    audio_file = "../audio/gTTS_test.mp3"
    transcript(audio_file)
