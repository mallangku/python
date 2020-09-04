# 이번에는 random 모듈과 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 내도록 프로그램을 바꿔 보세요.
# 같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.

import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data = line.strip().split(": ")
        eng_word, kor_word = data[0], data[1]
        vocab[eng_word] = kor_word

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    keys = list(vocab.keys())
    index = random.randint(0, len(keys)-1)
    eng_word = keys[index]
    kor_word = vocab[eng_word]

    # 유저 입력값 받기
    guess = input("{}: ".format(kor_word))

    # 프로그램 끝내기
    if guess == 'q':
        break

    # 정답 확인하기
    if guess == eng_word:
        print("맞았습니다!\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(eng_word))