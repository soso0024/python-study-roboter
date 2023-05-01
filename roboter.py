import csv

# ユーザからの入力を受け取る関数を定義する
def get_input():
    return input("Robota：あなたの名前を入力してください:")

# チャットボットからの出力を行う関数を定義する
def print_output(name):
    return print("こんにちは、" + name + "さん。")
    # or return f"こんにちは、{name}さん。"

# おすすめのアニメを聞く関数を定義する
def recommend_anime():
    return input("Robota：おすすめのアニメは何ですか？")

# おすすめのアニメを答える関数を定義する
def answer_anime(anime):
    return print("Robota：あなたのおすすめのアニメは、" + anime + "ですね。")

# 締めの挨拶をする関数を定義する
def say_goodbye():
    return print("Robota：ご利用ありがとうございました。")

# main関数を定義する
def main():
    while True:
        name = get_input()
        if name == "Robota：さようなら":
            break
        print_output(name)

        anime = recommend_anime()
        if anime == "Robota：さようなら":
            break
        if anime == "鬼滅の刃":
            print("Robota：ありきたりなおすすめですね。")
            break
        answer_anime(anime)
        break

    say_goodbye()

    # csvファイルから重複したアニメを検索し、カウントを増やす
    anime_count = {}
    with open('roboter-chatlog.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Name'] in anime_count:
                anime_count[row['Name']] += 1
            else:
                anime_count[row['Name']] = 1

    with open('roboter-chatlog.csv', 'a', newline='') as f:
        fieldnames = ['Name', 'Count']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # ファイルが空の場合はヘッダーを書き込む
        if f.tell() == 0:
            writer.writeheader()

        # アニメの名前をname列に書き込む
        writer.writerow({'Name': anime, 'Count': anime_count[anime]})
    
    print("ログを保存しました。")
    
# main関数を呼び出す
if __name__ == "__main__":
    main()
