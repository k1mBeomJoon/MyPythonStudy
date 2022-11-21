'''

'''

file = open('hello.txt', 'at')  # 기존 파일에 추가로 작성할 때는 at 사용
file.write('Hello.\n')
file.write('Nice to meet you.\n')
print('hello.txt 파일에 새로운 내용이 추가되었습니다.')
file.close()