'''
    for문과 range 함수
'''

dan = int(input('출력할 구구단을 입력하세요 >>> '))
for n in range(1, 10):  # range(1,10) -> 1~9 / range(10) -> 0~9
    print('{} x {} = {}'.format(dan, n, dan * n))


