import tkinter as tk
import pyaudio
import wave
import threading

# 録音の設定
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
OUTPUT_FILENAME = "../audio/output.wav"

# pyaudio の初期化
p = pyaudio.PyAudio()


# 録音開始
def start_recording():
    global frames, stream
    print("録音開始")
    frames = []
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    # 録音データを取得
    while recording_flag:
        data = stream.read(CHUNK)
        frames.append(data)


# 録音停止
def stop_recording():
    global recording_flag, stream
    print("録音停止")
    recording_flag = False
    stream.stop_stream()
    stream.close()
    p.terminate()

    # 録音したデータを WAV ファイルに保存
    with wave.open(OUTPUT_FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

    print(f"録音された音声は {OUTPUT_FILENAME} として保存されました。")


# 録音開始ボタン
def on_record_button_click():
    global recording_flag
    recording_flag = True
    threading.Thread(target=start_recording).start()  # 録音を別スレッドで実行


if __name__ == "__main__":
    # 録音の状態を管理するフラグ
    recording_flag = False

    # GUI ウィンドウの設定
    root = tk.Tk()
    root.title("録音アプリ")

    # 録音ボタン・停止ボタンの設定
    record_button = tk.Button(root, text="録音開始", command=on_record_button_click)
    record_button.pack(pady=10)
    stop_button = tk.Button(root, text="録音停止", command=stop_recording)
    stop_button.pack(pady=10)

    # GUI の開始
    root.mainloop()
