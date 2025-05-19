# 조별과제
# D3
from collections import Counter


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = list(input())
    a = []
    b = []
    # d = Counter(n)
    #
    # if d['?'] == 0:
    #     answer = d['L'] + d['?'] if d['L'] > d['R'] else d['R'] + d['?']
    # else :
    #     answer = abs(d['L']-d['R']) + d['?']
    cur = 0
    count = 0
    for i in n:
        if i == 'L':
            cur -=1
            a.append(cur)
        elif i == 'R':
            cur +=1
            a.append(cur)
        else :
            count +=1
            a.append(0)

    for i in a:
        b.append(abs(i))

    answer = max(b)




    print(f'#{test_case} {answer}')