import tkinter as tk
import pyaudio
import wave
import threading

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

    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    recording_flag = True
    while recording_flag:
        data = stream.read(CHUNK)
        frames.append(data)


# 録音を停止して音声ファイルを保存
def stop_recording():
    global recording_flag, stream, filename_entry, directory, voice_filename

    if not recording_flag:  # すでに録音が停止している場合は何もしない
        return

    print("録音停止")
    recording_flag = False
    stream.stop_stream()
    stream.close()
    p.terminate()

    voice_filename = filename_entry.get()
    if not voice_filename.endswith(".wav"):
        voice_filename += ".wav"
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
    global filename_entry, directory
    directory = folder
    root = tk.Tk()
    root.title("録音アプリ")

    tk.Label(root, text="保存ファイル名 (拡張子なし)").pack()
    filename_entry = tk.Entry(root)
    filename_entry.pack(pady=5)
    filename_entry.insert(0, "output")

    record_button = tk.Button(root, text="録音開始", command=on_record_button_click)
    record_button.pack(pady=10)
    stop_button = tk.Button(root, text="録音停止", command=stop_recording)
    stop_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    folder = "../audio"
    run_GUI(folder)
