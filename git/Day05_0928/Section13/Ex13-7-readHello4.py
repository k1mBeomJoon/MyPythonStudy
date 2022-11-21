'''

'''

file = open('hello.txt', 'rt')

line_list = file.readlines()    # 줄 별로 리스트에 넣음
print(line_list)
for line in line_list:
    print(line, end='')

file.close()