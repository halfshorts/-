import random as r
import time as t
count = 1
while True:
    number = []
    ans = []
    accord = 0
    bonus = 0
    s = 1
    print('제', count, '회 복권 추첨')
    playtype = str(input('수동 혹은 자동 입력:'))
    if playtype == '자동':
        while len(number) != 6:
            n = r.randint(1, 45)
            if n not in number:
                t.sleep(1)
                print(n)
                number.append(n)
    elif playtype == '수동':
        while len(number) != 6:
            t.sleep(1)
            print(s, '번째 숫자 입력')
            n = int(input())
            if n not in number and n <= 45 and n > 0:
                number.append(n)
                s = s + 1
            else:
                print('다시 입력하세요')
    else:
        print('구매 실패')
    t.sleep(1)
    print('제', count, '회 복권 당첨번호')
    while len(ans) != 6:
        n = r.randint(1, 45)
        if n not in ans:
            t.sleep(1)
            print(n)
            ans.append(n)
    t.sleep(1)
    print('보너스')
    t.sleep(1)
    while n in ans:
        n = r.randint(1, 45)
        if n not in ans:
            print(n)
    for i in number:
        if i in ans:
            accord = accord + 1
        if i == n:
            bonus = 1
    t.sleep(1)
    print('내 번호:', number)
    print('당첨 번호:', ans, '+', n)
    print('당첨번호', accord, '개 숫자 일치')
    if bonus == 1:
        print('보너스 숫자 일치')
    if accord == 6:
        print('1등, 3,023,630,672원 당첨')
    elif accord == 5 and bonus == 1:
        print('2등, 49,771,699원 당첨')
    elif accord == 5 and bonus == 0:
        print('3등, 1,375,472원 당첨')
    elif accord == 4:
        print('4등, 50,000원 당첨')
    elif accord == 3:
        print('5등, 5,000원 당첨')
    else:
        print('당첨 없음')
    t.sleep(1)
