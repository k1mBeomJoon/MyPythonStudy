'''
    메서드(method)
        특정 객체가 가지고 있는 함수를 의미
    -사용방법
    객체명.메서드명(매개변수)
    -메서드는 객체에 종속되어있음
'''

# String 객체 메서드 탐구

# format() 메서드
s = "10자리 폭 왼 쪽 정렬 '{:<10d}'"
print(s.format(123))
print("10자리 폭 오른쪽 정렬 '{:>10d}'".format(123))    # 파이썬에서는 문자열 자체를 객체로 인식해서, 문자열 뒤에 .format()을 쓸 수 있는 것임.
print("10자리 폭 가운데 정렬 '{:^10d}'".format(123))
print()
print("10자리 폭 왼 쪽 정렬 채움문자 '{:*<10d}'".format(123))
print("10자리 폭 오른쪽 정렬 채움문자 '{:*>10d}'".format(123))
print("10자리 폭 가운데 정렬 채움문자 '{:*^10d}'".format(123))

# count() 메서드
s = '내가 그린 기린 그림은 목이 긴 기린 그림이고, 네가 그린 기린 그림은 목 짧은 기린 그림이다,'
result = s.count('기린')
print('s 문자열 안에는 기린이라는 단어가 {}개 포함됨.'.format(result))

s = 'best of best best'
result = s.count('best', 5) # index값 5부터 뒤로 찾기 시작
print(result)
result = s.count('best', -7)    # 끝 index부터 7번 앞으로 온 후 뒤로 찾기 시작
print(result)

# find() 메서드 : 위치한 index 번호 반환(그 중 첫번째 index)
s = 'apple'
result = s.find('p')
print(result)
result = s.find('z')
print(result)       # 없는 것을 찾으라고 하면 -1이 반환됨.
if s.find('z') < 0:
    print("검색값이 존재하지 않습니다.")
s = 'best of best best'
result = s.find('best', 5)
print(result)

print()
# index() : find() 와 같지만 문자열이 존재하지 않을 경우 에러 발생.
# 에러발생 로그를 남겨놔야 하는 상황에는 index() 사용, 그렇지 않을 경우 find() 사용
s = 'apple'
result = s.index('p')
print(result)
result = s.index('z')
print(result)












