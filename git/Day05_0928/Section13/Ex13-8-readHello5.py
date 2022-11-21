'''

'''

file = open('hello.txt', 'rt')

line_list = file.readlines()    # 줄 별로 리스트에 넣음
print(line_list)
for no, line in enumerate(line_list):
    print('{} {}'.format(no+1, line), end='')

file.close()