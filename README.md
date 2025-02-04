# 仮想環境
- conda create -n interview python=3.10

# 機能
## 質問生成・対話機能(question.py)
- 入力
  - mode(str)
  - text(str)
- 出力
  - response.text(str)
- 入力内容に対する質問を生成
- １回の質問のみならず、対話による深堀りが可能
## 録音機能（record.py）
- 入力
  - filename(str)
  - 音声
- 出力
  - frames(list)
  - ../audio/filename.wav(音声データ)
- GUIで録音と停止を操作
- 録音中の音声を保存する
## 読み上げ機能（speech.py）
- 入力
  - question(str)
  - filepath(path)
- 出力
  - filename(mp3)
  - playing(音声)
- 生成された質問を音声ファイルに変換して、読み上げ
## 文字起こし機能
- 入力
  - audio_file(path)
- 出力
  - text(str)
- 音声ファイルから文字起こしして、文字列として返す