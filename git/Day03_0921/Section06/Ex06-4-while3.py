'''

'''

dan = 2
cnt = 1

    # 구분선 출력
while cnt < 90:
    print("-", end='')
    cnt += 1
print()

    # main
while dan <= 9:
    n = 1
    while n<=9:
        print('{}x{}={} '.format(dan, n, dan * n), end=' | ')
        n += 1
    dan += 1
    print()
    # 한 단이 끝나면 구분선 출력 후 줄바꿈
    cnt = 1
    while cnt < 90:
        print("-", end='')
        cnt += 1
    print()
