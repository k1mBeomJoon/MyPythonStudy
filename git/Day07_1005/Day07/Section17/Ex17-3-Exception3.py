'''

'''

# 예외처리 구체화 - 주로 잘 안하기도 하고, 필요시에는 보통 try 안에서 많이 해결함

# ValueError
# ZeroDivisionError

try:
    a = int(input('제수를 입력하세요. >>> '))
    b = int(input('피제수를 입력하세요. >>> '))
    print('{} / {} = {}'.format(a, b, a/b))
    print('예외 발생해도 실행됩니까?')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except ValueError:
    print('정수만 입력할 수 있습니다.')
except:
    print('예외가 발생했습니다.')