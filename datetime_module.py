import datetime
# 스탠다드 라이브러리에 있는 datetime 모듈은 '날짜'와 '시간'을 다루기 위한 다양한 '클래스'를 갖추고 있습니다.


# datetime 값 생성
# 2020년 3월 14일을 파이썬으로 어떻게 표현할 수 있을까요? 이렇게 하면 됩니다.
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)  #2020-03-14 00:00:00
print(type(pi_day))  #<class 'datetime.datetime'>

# 보시다시피 시간은 자동으로 00시 00분 00초로 설정되었는데요. 우리가 시간까지도 직접 정할 수 있습니다.
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(pi_day)  #2020-03-14 13:06:15
print(type(pi_day))  #<class 'datetime.datetime'>

# 오늘 날짜
# 우리가 날짜와 시간을 정해 주는 게 아니라, 코드를 실행한 '지금 이 순간'의 날짜와 시간을 받아 오고 싶다면? 이렇게 하면 됩니다.
today = datetime.datetime.now()
print(today)  #2020-04-05 17:49:12.360266
print(type(today))  #<class 'datetime.datetime'>



# timedelta
# 두 datetime 값 사이의 기간을 알고 싶으면, 마치 숫자 뺄셈을 하듯이 그냥 빼면 됩니다.
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)  #22 days, 4:42:57.360266
print(type(today - pi_day))  #<class 'datetime.timedelta'>
# 보시다시피 두 datetime 값을 빼면, timedelta라는 타입이 나오는데요. 이건 날짜 간의 차이를 나타내는 타입이라고 생각하시면 됩니다.

# 반대로 timedelta를 생성해서 datetime 값에 더해 줄 수도 있습니다.
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=5, hours=3, minutes=10, seconds=50)
print(today)  #2020-04-05 17:54:24.221660
print(today + my_timedelta)  #2020-04-10 21:05:14.221660



# datetime 해부하기
# datetime 값에서 '연도'나 '월' 같은 값들을 추출하려면 어떻게 해야 할까요?
today = datetime.datetime.now()
print(today)  #2020-04-05 17:59:21.709817
print(today.year)  # 연도 2020
print(today.month)  # 월 4
print(today.day)  # 일 5
print(today.hour)  # 시 17
print(today.minute)  # 분 59
print(today.second)  # 초 21
print(today.microsecond)  # 마이크로초 709817



# datetime 포맷팅
# datetime 값을 출력하면 별로 예쁘지 않습니다. 하지만 strftime을 사용하면, 우리 입맛대로 바꿀 수 있습니다.
today = datetime.datetime.now()
print(today)  #2020-04-05 18:09:55.233501
print(today.strftime("%A, %B %dth %Y"))  #Sunday, April 05th 2020