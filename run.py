from app import app_run

if __name__ == "__main__":
    user_input = "私は、大学の研究でガラスの上に銀薄膜の島状構造を作り、光増強性能を評価する研究を行っています。実験装置の改造を行い、実験条件を2倍に広げることに成功しました。"
    directory = "audio"
    filename = "question"
    mode = "自己PR"
    app_run(user_input, directory, filename, mode)
