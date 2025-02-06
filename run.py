from app import app_run

if __name__ == "__main__":
    mode = input(
        "モードを選択してください　※ 自己PR, 学生時代に頑張ったこと, 志望動機など　\nモード："
    )
    user_input = input(f"{mode}を入力してください　\n{mode}：")
    directory = "audio"
    filename = "question"
    app_run(user_input, directory, filename, mode)
