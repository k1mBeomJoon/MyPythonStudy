'''
    지역변수(local)
        함수 내부 선언
        함수 내부에서만 사용 가능
    전역변수(global)
        함수 외부 선언
        함수 내부 외부 모두 사용 가능
'''

# gVar = '전역'
# def globalAndLocal():
#     lVar = '지역'
#     print(gVar, '변수 입니다.')  # 전역변수 참조만 하고 있다.
#     print(lVar, '변수 입니다.')
#
# globalAndLocal()



gVar = '전역'
def globalAndLocal():
    lVar = '지역'
    gVar = '변경된 전역이 아닌 새로운 지역'
    print(gVar, '변수 입니다.')
    print(lVar, '변수 입니다.')

globalAndLocal()
print(gVar)
print()


# 전역변수 선언
total = 0
wedding = {}
def gift(dic, who, money):
    global total    # 전역변수 total을 사용하겠다. 예를 들어 전역변수의 값을 수정하고 싶을 때, 이와 같이 선언 한 후 값을 수정해야 한다.
    total += money
    dic[who] = money

gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
gift(wedding, '고모', 20)
print('축의금 명단 : {}'.format(wedding))
print('전체 축의금 : {}'.format(total))

