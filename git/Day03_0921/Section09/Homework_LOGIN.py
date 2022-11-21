#     # [ 초기화면 ]
# print('[  회원가입  ]')
# Total_T = True
# while Total_T:
#     # [ ID body ]
#     ID_T = True
#     ID_save = 'default'
#     while ID_T:
#         ID = input('사용할 ID를 입력하세요(5글자 이상, 영문, 숫자 혼합) >>> ')
#         IDAlp_cnt = 0
#         IDNum_cnt = 0
#         for ch in ID:
#             if ch.isalpha():
#                 IDAlp_cnt += 1
#             elif ch.isnumeric():
#                 IDNum_cnt = + 1
#         if IDAlp_cnt > 0 and IDNum_cnt:
#             if IDAlp_cnt + IDNum_cnt > 4:
#                 print('{}는 사용 가능한 ID 입니다 !'.format(ID))
#                 ID_save = ID
#                 ID_T = False
#             else:
#                 print('{}는 사용 불가능한 아이디 입니다. 조건에 맞춰 다시 입력해 주세요.'.format(ID))
#                 continue
#         else:
#             print('{}는 사용 불가능한 아이디 입니다. 조건에 맞춰 다시 입력해 주세요.'.format(ID))
#             continue
#
#         # [ PW body ]
#     PW_T = True
#     PW_save = 'default'
#     while PW_T:
#         PW = input('사용할 PW를 입역하세요(영문,숫자 포함 8자 이상) >>> ')
#         PWAlp_cnt = 0
#         PWNum_cnt = 0
#         for ch in PW:
#             if ch.isalpha():
#                 PWAlp_cnt += 1
#             elif ch.isnumeric():
#                 PWNum_cnt = + 1
#         if PWAlp_cnt > 0 and PWNum_cnt > 0:
#             if PWAlp_cnt + PWNum_cnt >= 8:
#                 print('{}는 사용 가능한 PW 입니다 !'.format(PW))
#                 PW_save = PW
#                 PW_T = False
#             else:
#                 print('{}는 사용 불가능한 PW입니다. 조건에 맞춰 다시 입력해주세요.'.format(PW))
#                 continue
#         else:
#             print('{}는 사용 불가능한 PW입니다. 조건에 맞춰 다시 입력해 주세요.'.format(PW))
#             continue
#
#         #  [ PW 2차 확인 ]
#     PW2_T = True
#     while PW2_T:
#         PW2 = input('PW확인을 위해 한번 더 입력해주세요. >>> ')
#         if PW2 == PW_save:
#             print('PW가 일치합니다 ! ')
#             print('회원가입이 완료되었습니다 !')
#             choice = input('1. 로그인 창으로 이동 / 2. 프로그램 종료 >>> ')
#             if choice == 1:
#                 # [ 로그인 ]
#                 # [ ID 입력 ]
#                 LogID_T = True
#                 while LogID_T:
#                     print('[ 로그인 ]')
#                     LogID = input('로그인을 위해 ID를 입력해주세요. >>> ')
#                     if LogID == ID_save:
#                         LogPW = input('PW를 입력해주세요. >>> ')
#                         if LogPW == PW_save:
#                             print('로그인이 완료되었습니다. {}님, 환영합니다 !'.format(ID_save))
#                             Total_T = False
#                         else:
#                             print('PW가 일치하지 않습니다. 다시 입력해주세요.')
#                             LogID_T = False
#                     else:
#                         print('등록되지 않은 아이디 입니다. 다시 입력해주세요.')
#                         continue
#             elif choice == 2:
#                 print('프로그램을 종료합니다.')
#                 break
#                 # Total_T = False # 프로그램 종료 / 왜 안돼?
#             else:
#                 print('숫자가 정확하지 않습니다. 숫자를 다시 입력해주세요.')
#                 continue
#         else:
#             print('PW가 일치하지 않습니다. 다시 시도해주세요.')
#             continue
#         break
#     break



# -------------------------------------------------------------------------------------------------------------------------------------------------------


id = None
pwd = None

# 아이디 입력
while True:
    id = input('아이디를 입력하세요 (3글자 이상) >>> ')
    if len(id) >= 3:
        break
    else:
        print('>> 3글자 이상 입력해주세요.')

    # 패스워드 입력
while True:
    pwd = input('패스워드를 입력해주세요. (영문, 숫자 혼합 8자 이상) >>> ')

    if len(pwd) < 8:
        print('>> 조건에 맞게 다시 입력해주세요.')
        continue
    '''
    hasContainAlpha = False
    hasContainNum = False
    
    for ch in pwd:
        if ch.isalpha():
            hasContainAlpha = True
        elif ch.isnumeric():
            hasContainNum = True

    if not hasContainAlpha:
        print('>> 조건에 맞게 다시 입력해주세요.')
        continue
    if not hasContainNum:
        print('>> 조건에 맞게 다시 입력해주세요.')
        
    # 위 주석처리된 부분의 코드가 접근 불가라고 주의 표시가 뜨고 제대로 작동하지 x.
    # 때문에 아랫부분 cnt변수를 선언하여 이를 이용하여 카운트하는 방식으로 변경.
    '''
    alpCnt = 0
    numCnt = 0
    for ch in pwd:
        if ch.isalpha():
            alpCnt += 1
        if ch.isnumeric():
            numCnt += 1

    if alpCnt < 1 or numCnt < 1:
        print('>> 조건에 맞게 다시 입력해주세요.')
        continue

    pwdCheck = input('패스워드 확인을 위해 한번 더 입력해주세요. >>> ')
    if pwdCheck != pwd:
        print('>> 패스워드가 일치하지 않습니다. 다시 입력해주세요.')
        continue
    break

    # 로그인 or 프로그램 종료
choice = input('>> 회원가입이 완료되었습니다. \n>> 1. 로그인 / 2. 프로그램 종료 >>> ')
while True:
    if choice == '1':
        print('[ 로그인 ]')
        loginId = input('아이디를 입력하세요. >>> ')
        loginPwd = input('패스워드를 입력하세요. >>> ')
        if loginId != id:
            print('>> 등록되지 않은 아이디입니다.')
            continue
        if loginPwd != pwd:
            print('>> 패스워드가 일치하지 않습니다.')
            continue
        print('>> 로그인 완료!')
        break
    elif choice == '2':
        print('프로그램 종료!')
        break

# 기능 완전하게 구현 완료 !