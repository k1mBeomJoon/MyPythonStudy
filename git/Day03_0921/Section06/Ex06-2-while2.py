'''
    while문 예제
'''

my_list = []
n = int(input('정수를 입력하세요(종료는 0) >>> '))
while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0) >>> '))

print(my_list)