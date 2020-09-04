import random

ANSWER = random.randint(1, 20)
NUM_TRIES = 4

while 1 <= NUM_TRIES <= 4:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞춰 보세요: ".format(NUM_TRIES)))
    if guess != ANSWER:
        if guess < ANSWER :
            print("Up")
        elif guess > ANSWER :
            print("Down")
    else:
        print("축하합니다. {}번만에 숫자를 맞추셨습니다.".format(5-NUM_TRIES))
        break
    NUM_TRIES -= 1
    if NUM_TRIES == 0:
        print("아쉽습니다. 정답은 {}였습니다.".format(ANSWER))