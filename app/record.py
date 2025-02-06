import tkinter as tk
import pyaudio
import wave
import threading
from .speech import idx

global voice_filename
voice_filename = "output.wav"

# 録音の設定
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# pyaudio の初期化
p = pyaudio.PyAudio()
recording_flag = False


# 録音データを格納するリスト
def start_recording():
    global frames, stream, recording_flag
    print("録音開始")
    frames = []

    input_device_index = select_device()  # デバイスの選択

    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        input_device_index=input_device_index,
    )

    recording_flag = True
    while recording_flag:
        data = stream.read(CHUNK)
        frames.append(data)


# 入力デバイスを選択
def select_device():
    p = pyaudio.PyAudio()  # pyaudio の初期化
    input_device_index = None
    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(
            f"Device {i}: {info['name'].encode('shift-jis').decode('utf-8', errors='ignore')}"
        )
        if "マイク" or "Microphone" in info["name"]:  # 適切なデバイス名を指定
            input_device_index = i
            break

    if input_device_index is None:
        print(
            "適切な入力デバイスが見つかりませんでした。デフォルトのデバイスを使用します。"
        )
        input_device_index = p.get_default_input_device_info()["index"]
    return input_device_index


# 録音を停止して音声ファイルを保存
def stop_recording():
    global recording_flag, stream, directory, voice_filename

    if not recording_flag:  # すでに録音が停止している場合は何もしない
        return

    print("録音停止")
    recording_flag = False
    stream.stop_stream()
    stream.close()
    p.terminate()

    save_voicefile(directory, voice_filename)  # 音声ファイルを保存


# 音声ファイルを保存
def save_voicefile(directory, voice_filename):
    voice_path = f"{directory}/{voice_filename}"
    with wave.open(voice_path, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

    print(f"録音された音声は {voice_filename} (voice_filename) として保存されました。")


# 録音ボタンが押されたときの処理
def on_record_button_click():
    global recording_flag
    recording_flag = True
    threading.Thread(target=start_recording).start()


# GUI を表示
def run_GUI(folder):
    global directory
    directory = folder

    root = tk.Tk()
    root.title("録音アプリ")
    record_button = tk.Button(root, text="録音開始", command=on_record_button_click)
    record_button.pack(pady=10)
    stop_button = tk.Button(root, text="録音停止", command=stop_recording)
    stop_button.pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    folder = "../audio"
    run_GUI(folder)
