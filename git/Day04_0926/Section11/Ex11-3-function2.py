'''

'''
# 코드 정렬 팁 : Ctrl + Alt + L

def get_average(marks):
    total = 0
    for subject in marks:
        total += marks[subject]
    average = total / len(marks)
    return average

marks = {'국어': 90, '영어': 90, '수학': 85}
average = get_average(marks)
print('평균은 {}점 입니다.'.format(average))

'''
    for문에서의 딕셔너리 사용 공부 할 것.
'''