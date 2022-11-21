'''
    변수(variable)
    어떤 데이터를 저장하고자 할 때 서용하는 메모리 저장소.\

    변수명 규칙
    영문, 한글, 숫자, 밑줄로 구성된다.
    특수문자는 사용 할 수 없음.
    대소문자를 구별.
    변수명의 첫 글자를 숫자로 사용할 수 없음.
    예약어, 키워드(list, dict, if, for, and 등)는 사용할 수 없음.
'''

name = 'Alice'
age = 25
address = ''' 우편번호 12345 서울시 영등포구 여의도동 1234-5 '''
    # 변수 선언 문장에 홑따옴표 3개를 쓰면 주석이 아님.

print(address)

# 잘못된 변수명 예시
# 2myvar = 'python1'
# my-var = 'python2'
# my var = 'python3'

# 주석 단축키 : Ctrl + /

'''
    여러 값 할당 
    python을 사용하면 한 줄에 여러 변수에 값을 할당할 수 있다.
'''
x, y, z = "피카츄", "라이츄", "파이리"
print(x)
print(y)
print(z)

# Ctrl + D : 줄 복사
# Ctrl + Y : 줄 삭제

'''
    여러 변수에 대한 하나의 값
    : 한 줄에서 여러 변수에 동일한 값을 할당할 수 있음.
'''
x = y = z = "꼬부기"
print(x)
print(y)
print(z)

