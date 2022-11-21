'''
    [  예외처리  정리  ]

    try:
        코드 작성영역
    except:
        예외 발생 시 처리 영역
    else:
        예외가 발생하지 않으면 처리되는 영역
    finally:
        언제나 실행되는 영역
'''

try:
    a = int(input('제수를 입력하세요. >>> '))
    b = int(input('피제수를 입력하세요. >>> '))
    result = a / b
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except:
    print('예외가 발생했습니다.')
else:                                       # try문 안에서 예외가 발생하지 않으면 else가 실행됨. 굳이 else 안쓰고  try 안에서 처리해도 됨.
    print('{} / {} = {}'.format(a, b, result))
finally:                                    # 반드시 실행되어야 하는 코드 / 예를 들면 파일 I/O 에서 'file close'
    print('프로그램을 종료합니다.')

# github - Jpub 에서 코딩 연습.