from collections import deque

t = int(input())
for test in range(1,t+1):
    n, m = map(int, input().split())

    ml = list(map(int, input().split()))

    pizza = deque()
    for i in range(1,m+1):
        # 피자번호, 치즈의 개수
        pizza.append((i, ml[i-1]))
    answer = []
    myqueue = deque()
    for i in range(n):
        idx, cheese = pizza.popleft()
        myqueue.append((idx,cheese))

    answer = []
    while myqueue:
        # 피자를 빼고 치즈를 분해
        idx, cheese =myqueue.popleft()
        cheese = cheese//2

        # 만약 0이라면 빼고 새로운 피자를 넣는다
        if cheese == 0:
            answer.append(idx)
            if pizza:
                idx, cheese = pizza.popleft()
                myqueue.append((idx,cheese))
            continue
        # 만약 다 안녹았으면 그대로 넣고 다시 돌린다.
        myqueue.append((idx,cheese))
    print(f'#{test} {answer[-1]}')

