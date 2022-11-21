'''
    continue
        while문이나 for문과 같은 반복문을 강제로 건너뛰기(아래코드 실행하지 않는다)
'''

    # a 부터 b 까지의 숫자 중 3의 배수를 제외한 수의 합
total = 0
a = int(input("숫자 입력 >>> "))
print()
b = int(input("숫자 입력 >>> ")) + 1
print()

for a in range(a, b):
    if a % 3 == 0:  # 3의 배수
        continue    # 3의 배수는 total에는 더하지 않겠다
    print('a : {}, total : {}'.format(a, total))
    total += a
print('total : {}'.format(total))
