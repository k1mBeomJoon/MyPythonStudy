'''
    다르게 쓰면 ?
'''

my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0) >>> '))
    my_list.append(n)

my_list.pop()   # my_list의 마지막 요소는 언제나 0이므로 제거합니다.
print(my_list)