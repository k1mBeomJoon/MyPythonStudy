'''
    별명 사용하기
    - 실무에서 많이 사용
'''

import converter as cvt # converter라는 module을 cvt 라는 별명으로 사용

miles = cvt.kilometer_to_miles(150)
print('150km={}miles'.format(miles))

pounds = cvt.gram_to_pounds(1000)
print('1000g={}pounds'.format(pounds))
