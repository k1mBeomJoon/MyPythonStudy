'''
    I/O (파일 입출력)
        입력(input) : 기존파일 읽어들임
        출력(output) : 파일생성, 내용 추가
'''

# Output

# 방법 1
# file = open('myFile.txt', 'wt') # 바이트로 쓰고 싶을 때는 wt 대신 wb. 다른 방식 궁금하면 open에 커서 올려서 사이트 참조
# print('myFile.txt 파일이 생성되었습니다.')
# file.close()    # 반드시 파일을 닫아줘야됨.

# 방법 2
# with 문 - 자동으로 close()를 해줌
with open('myFile.txt', 'wt') as file:
    print('myFile.txt 파일이 생성되었습니다.')


