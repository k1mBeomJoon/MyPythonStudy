'''

'''

import sys

file = open('hello.txt', 'rt')

line_list = file.readlines()
sys.stdout.writelines(line_list)    # print문이 아닌 sys모듈을 이용하여 출력해보기
print(line_list)

file.close()