'''
    csv module을 import 하여 사용
'''
'''
방법 1
import csv
with open('차량관리.csv', 'w') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([1, '25다2345', '2020-10-20,14:20'])
    csv_maker.writerow([1, '28하3456', '2020-10-20,14:40'])
print('차량관리.csv 파일이 생성되었습니다.')
'''

'''
# 방법 2
import csv
with open('차량관리.csv', 'w', newline='') as file:
    csv_maker = csv.writer(file, delimiter=',')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([1, '25다2345', '2020-10-20,14:20'])
    csv_maker.writerow([1, '28하3456', '2020-10-20,14:40'])
print('차량관리.csv 파일이 생성되었습니다.')
'''


# 방법 3
import csv
with open('차량관리.csv', 'w', newline='') as file:
    csv_maker = csv.writer(file, delimiter=',', quotechar='"')
    csv_maker.writerow([1, '08러1234', '2020-10-20,14:00'])
    csv_maker.writerow([1, '25다2345', '2020-10-20,14:20'])
    csv_maker.writerow([1, '28하3456', '2020-10-20,14:40'])
print('차량관리.csv 파일이 생성되었습니다.')
