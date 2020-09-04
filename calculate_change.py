def calculate_change(payment, cost):
    # 코드를 작성하세요.
    change = payment - cost  # 67000
    fifty_thousand = int(change / 50000)
    print("{}원 지폐: {}장".format(50000, fifty_thousand))

    change = change % 50000
    ten_thousand = int(change / 10000)
    print("{}원 지폐: {}장".format(10000, ten_thousand))

    change = change % 10000
    five_thousand = int(change / 5000)
    print("{}원 지폐: {}장".format(5000, five_thousand))

    change = change % 5000
    one_thousand = int(change / 1000)
    print("{}원 지폐: {}장".format(1000, one_thousand))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)