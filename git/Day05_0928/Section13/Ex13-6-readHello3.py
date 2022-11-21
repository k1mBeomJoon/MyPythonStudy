'''

'''

file = open('hello.txt', 'rt')

while True:
    str = file.readline()
    print(str)
    if str == '':
        break
    # print(str, end='')

file.close()