'''
    Lotto
'''

import random
import time

pot = [n for n in range(1, 46)] # pot 리스트에 1~45까지 전부 담음
print('pot : {}'.format(pot))
jackpot = []                    # 빈 리스트 jackpot 하나 생성

for n in range(1, 7):
    random.shuffle(pot)         # 순서를 섞어
    pick = pot.pop()            # 제일 마지막 값을 뽑아, 그리고 그 값을 지워, 그걸 pick에 담아
    print('{}번째 당첨번호는 {}입니다.'.format(n, pick))  #  n번째 pop된 수를 화면에 출력해줘
    jackpot.append(pick)    # 뽑힌 값(pick)을 빈 리스트인 jackpot에 담아줘
    time.sleep(0.3)           # 1초 일시중지 했다가 다음번 실행해

jackpot.sort()              # 임의로 뽑힌 6개의 숫자들을 오름차순으로 정리해줘
print('이번 당첨번호는 {} 입니다.'.format(jackpot))       # 결과 출력
pot.sort()
print('실행 후 pot : {}'.format(pot))
