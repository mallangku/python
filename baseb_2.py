
# 사용자에게서 숫자 3개 입력받기

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        user_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))

        if user_num < 0 or user_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif user_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(user_num)

    return new_guess


print(take_guess())