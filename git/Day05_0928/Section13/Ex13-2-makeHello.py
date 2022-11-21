'''

'''

file = open('hello.txt', 'wt')  # wt는 기존거 없애고 새로 작성
file.write('Hello.')    # write() 메서드로 파일에 작성
file.write('\n')
file.write('Welcome.')
file.write('\n')
print('hello.txt 파일이 생성되었습니다.')
file.close()