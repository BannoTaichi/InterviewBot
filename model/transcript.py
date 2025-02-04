import speech_recognition as sr
from pydub import AudioSegment

# 音声認識用のインスタンスを生成
recognizer = sr.Recognizer()


# MP3 を WAV に変換
def mp3_to_wav(audio_file):
    sound = AudioSegment.from_mp3(audio_file)

    new_path = audio_file.replace(".mp3", "_converted.wav")
    sound.export(new_path, format="wav")
    print("MP3 を WAV に変換しました！")
    return new_path


# WAV ファイルの文字起こし
def transcript(audio_file, directory="../audio"):
    path = f"{directory}/{audio_file}"
    if audio_file.endswith(".mp3"):
        path = mp3_to_wav(path)

    with sr.AudioFile(path) as source:
        print("音声を認識中...")
        audio_data = recognizer.record(source)  # 音声データを取得

    # GoogleのSpeech-to-Text APIで文字起こし（日本語対応）
    try:
        text = recognizer.recognize_google(audio_data, language="ja-JP")
        print("認識結果:", text)
        return text
    except sr.UnknownValueError:
        print("音声を認識できませんでした")
    except sr.RequestError:
        print("Google Speech API に接続できませんでした")


if __name__ == "__main__":
    audio_file = "gTTS_test.mp3"
    transcript(audio_file)
