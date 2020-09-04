# data 폴더의 chicken.txt 파일을 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요.
# 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다.

with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    total_revenue = 0
    total_days = 0

    for line in f:
        data = line.strip().split(": ")
        revenue = int(data[1])  # 그날의 매출

        total_revenue += revenue
        total_days += 1

print(total_revenue/total_days)