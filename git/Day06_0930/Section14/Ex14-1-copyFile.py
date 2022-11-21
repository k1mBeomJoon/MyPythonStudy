'''
    파일 복사
        원본 파일을 변수화시켜 (=변수로 받아서 =메모리에 올린다) 복사본을 사용
'''

buffer_size = 1024 # 1024Byte로, 1KB를 의미함
with open('hello.txt', 'rb') as source:
    with open('hello2.txt', 'wb') as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer: # if buffer == '':
                break
            copy.write(buffer)

# with 썼음으로 close 할 필요 없음.
print('hello2.txt 파일이 복사되었습니다.')

