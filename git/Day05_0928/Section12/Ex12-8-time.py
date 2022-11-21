'''
    time module
        시간 처리에 관련된 module
'''

import time

# 1970.01.01 0시 0분 0초 부터 현재까지의 경과 시간을 반환
# 마이크로초까지 반환
print(time.time())

# ctime() 함수 - 인수로 전달된 time 시간 형식을 갖춰 반환
print(time.ctime(time.time()))

# strftime() 함수 : 인수로 전달된 날짜와 지시자를 이용하여 형식을 갖춘 날짜 데이터를 문자열로 반환
print(time.strftime('%Y-%m-%d %H:%M:%S'))   # %Y, %m 등이 지시자임. 다른 지시자가 궁금하면 strftime에 커서 올려서 제일 아래 링크 참조
# 한글로 쓰고 싶을 때 방법. 이렇게 안하고 한글 쓰면 ERR.
print(time.strftime('%Y년 %m월 %d일'.encode('unicode-escape').decode()).encode().decode('unicode-escape'))

# 인자 초 만큼 일시중지
time.sleep(1)
print('중지끝')

# 간단한 카운트 세는 코드
sec = 1
while True:
    print(sec)
    if sec == 10:
        break
    time.sleep(1)
    sec += 1