# 이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내 주는 프로그램을 만들려고 합니다.
# 프로그램은 콘솔에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다.
# 사용자가 입력한 영어 단어가 정답이면 "맞았습니다!"라고 출력하고, 틀리면 "아쉽습니다. 정답은 OOO입니다."가 출력되어야 합니다.

with open('vocabulary.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        data = line.strip().split(": ")
        eng_word, kot_word = data[0], data[1]

        # 유저 입력값 받기
        guess = input("{}: ".format(kot_word))

        # 정답 확인하기
        if guess == eng_word :
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(eng_word))