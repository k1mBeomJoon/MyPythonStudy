'''
    random
        난수 생성 모듈
'''

import random
# 두 인수(매개변수) 사이의 난수 발생
print(random.randint(1, 10))    # 1 ~ 10 중 난수 발생

# range 함수와 비슷
print(random.randrange(10))     # 0 ~ 9 중 난수 발생
print(random.randrange(1, 10))     # 1 ~ 9 중 난수 발생
print(random.randrange(1, 10, 2))     # 1 ~ 9 중 홀수만 발생 / 세번째 인수는 'step' : 첫번째 인수부터 step만큼 더한 것들 중 발생

# 0 이상 1 미만
print(random.random())  # random 모듈의 random 함수 - 가장 많이 씀. 여기에 100을 곱하면 100프로 단위 확률이 나옴.

if random.random() < 0.5:
    print('당첨')
else:
    print('꽝')

# choice 함수

seasons = ['spring', 'summer', 'fall', 'winter']
print(random.choice(seasons))

# shuffle 함수 - 임의로 섞는 함수
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)