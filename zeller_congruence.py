import math


def day():
    """日付の情報入力を行う
    
    zeller関数に直接数値を入力することでも曜日を判定することができるが、day関数を用いることで、zellerの公式の使用条件を十分に満たすことができ、ミスが減る。これにday関数の意義を見出す。

    0を入力することで、一つ前の入力に戻ることができる。

    :return: 日付の情報（西暦、月、日）
    """
    year = int(input("何年かを西暦で入力してください："))

    while True:
        month = int(input("何月なのかを入力してください："))
        if month == 0:
            year = int(input("何年かを西暦で入力してください："))
        else:
            break

    while True:
        date = int(input("何日なのかを入力してください："))
        if date == 0:
            while True:
                month = int(input("何月なのかを入力してください："))
                if month == 0:
                    year = int(input("何年かを西暦で入力してください："))
                else:
                    break
        else:
            break
    
    if month == 1:
        month =13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1

    return year, month, date


def zeller(year, month, date):
    """ツェラーの公式を適用し曜日を判定する
    
    :param year: 西暦（グレゴリオ暦）
    :param month: 月（ただし、1月は前年の13月、2月は前年の14月とする）
    :param date: 日

    return: 判定結果
    """
    Y = year % 100
    h = (date + math.floor(26 * (month + 1) / 10) + Y + math.floor(Y / 4) -2 * math.floor(year / 100) + math.floor(year / 400)) % 7

    answers = ["土曜日です。","日曜日です。","月曜日です。","火曜日です。","水曜日です。","木曜日です。","金曜日です。"]
    
    return answers[h]

if __name__ == "__main__":
    # 使い方説明
    print("あなたの考えている日付の曜日、教えます。")
    print("注意：1月、2月の曜日を知りたいときは、前年の13月、14月としてください。例えば2023年1月ならば、2022年13月です。また、前問に戻りたい場合は、0と入力してください。また、半角数字のみで入力してください。半角で入力しないとエラーが起こります。")
    
    # 実行コード
    unknown_year, unknown_month, unknown_date = day()
    print(zeller(unknown_year, unknown_month, unknown_date))
