'''
    set
'''

# 교집합
# 방법1 : 연산자 사용
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 & s2)
# 방법2 : 메서드 사용
result = s1.intersection(s2)
print(result)

# 합집합
# 방법1 : 연산자 사용
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 | s2)
# 방법2 : 메서드 사용
result = s1.union(s2)
print(result)

# 차집합
# 방법1 : 연산자 사용
s1 = {'apple', 'banana', 'cherry'}
s2 = {'apple', 'banana', 'orange'}
print(s1 - s2)
# 방법2 : 메서드 사용
result = s1.difference(s2)
print(result)
