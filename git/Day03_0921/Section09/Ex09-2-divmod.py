'''
    divmod
        두 숫자를 인자로 전달받아 첫번째 인자를 두번째 인자로 나눈 몫과 나머지를 tuple 형식으로 변환
        index[0]에 몫을 저장, index[1]에 나머지를 저장
'''

money = 10000
price = 3000
result = divmod(money, price)
print('방을 {}개 사고 {}원이 남았습니다.'.format(result[0], result[1]))