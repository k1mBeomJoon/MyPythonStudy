'''
    사용자 함수
        사용자가 직접 만든 함수

    -사용방법
    def 함수이름(매개변수):
        본문
        return
'''

# welcome()함수 정의
def welcome():
    print('Hello Python')
    print('Nice to meet you')

welcome()   # 함수 호출
print()


# 매개변수가 있는 함수
def intoduce(name, age):
    print('내 이름은 {}이고, 나이는 {}살 입니다.'.format(name, age))

intoduce('james', '25')


# 가변 매개변수 함수
def show(*args):
    for item in args:
        print(item, end=' ')

show('python')
print()
show('python', 'Java', 'C++')
print()
print()

# 반환(return)값이 있는 함수
def address():
    str = '우편번호 12345\n'
    str += '서울시 영등포구 여의도동'
    return str

result = address()
print(result)
print()

# 더하기 함수
def plus(num1, num2):
    return num1 + num2

print(plus(1, 3))
print()

# 옆으로 한 칸 이동
area = 0
def move():
    return area + 1
print('유닛이 {}칸 이동했습니다.'.format(move()))


