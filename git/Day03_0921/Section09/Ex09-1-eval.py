'''
    eval
        매개변수로 받은 expression(=식)을 문자열로 받아서 실행하는 함수
'''
    # 내장함수는 겁나 많고, 알아두면 좋은게 많으니 찾아보기

expr = input('계산식을 입력하세요 >>> ')
result = eval(expr)
print(expr + ' = ' + str(result))