# join()
s = '-'.join('python')
print(s)

s = '/'.join(['a', 'b', 'c', 'd', 'e'])
print(s)
s = ''.join(['a', 'b', 'c', 'd', 'e'])
print(s)
s = ''.join({'a' : 'apple', 'b' : 'banana'})
print(s)

# spilt()-자주 사용 : 문자열을 공백을 기준으로 나누어서 list형태로 list[str]로 반환
s = 'Life is too short'
result = s.split()
print(result)

# 자주 사용
s = '010-2401-1841'
result = s.split('-')
print(result)
# 뒷번호만?
print(result[2])

# replace() : 치환
s = 'Life is too short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() : 공백제거
s = '      apple'
print(s)
print()
result = s.lstrip()
print(result)

s = 'apple      '
result = s.rstrip()
print(result)

s = '   apple      '
result = s.strip()
print(result)

print()
s = ' a p p l e  '
result = s.replace(' ', '')
print(result)