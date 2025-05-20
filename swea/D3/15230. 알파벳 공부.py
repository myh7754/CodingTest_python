from collections import deque

t = int(input())

for test in range(1,t+1):
    data = 'abcdefghijklmnopqrstuvwxyz'

    queue = deque()
    # 이거 26개 빠르게 담는방법 없음?
    for i in data:
        queue.append(i)
    s = deque(input())
    count = 0

    for x,y in zip(s,queue):
        if x == y:
            count +=1
        if x != y:
            break

    print(f'#{test} {count}')

