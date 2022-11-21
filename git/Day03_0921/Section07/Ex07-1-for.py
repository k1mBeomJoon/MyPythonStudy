'''
    for문
        값의 범위나 횟수가 정해져 있을 때 사용하면 편리한 반복문
        while문보다 자주 사용한다.
        
    for 변수 in 반복가능한객체:
        반복실행문
'''

    # 숫자와 영문이 혼합된 비밀번호만을 받기 위한 코드
pwd = input('비밀번호를 입력하세요 >>> ') # 반복가능한객체
ch_count = 0
num_count = 0

for ch in pwd:
    if ch.isalpha():    # is alphabet?
        ch_count += 1
    elif ch.isnumeric():    # is numeric?
        num_count =+ 1
if ch_count > 0 and num_count > 0:
    print('가능한 비밀번호 입니다.')
else:
    print('불가능한 비밀번호 입니다.')

print('pwd : {}'.format(pwd))