'''

'''

file = open('hello.txt', 'rt')

while True:
    str = file.read(5)
    print(str)  # 5개씩 읽는지 확인하려고 여기에 찍고 아래 주석처리. 개행이랑 공백 때문에 이상하게 읽히는 것 같은데 파일에서 개행이랑 공백 다 지우면 정상적으로 나옴.
    if not str:
        break
    # print(str, end='')

file.close()