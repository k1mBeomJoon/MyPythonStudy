'''
    CSV(comma-sepearate values)
        몇가지 필드를 쉼포(,)로 구분한 데이터 및 텍스트 파일이다.
'''

student_list = []
with open('studentList.csv', 'rt', encoding='UTF-8') as file:
    file.readline() # csv파일에서 첫 줄을 날림(속성을 날림)
    while True:
        line = file.readline()
        if not line:
            break
        student = line.split(',')
        student_list.append(student)
print(student_list)
