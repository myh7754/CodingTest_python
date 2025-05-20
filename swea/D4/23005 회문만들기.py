# 회문만들기
# D4

from collections import deque

t = int(input())
for _ in range(t):
    s = input()
    if s == s[::-1]:
        print(0)
        continue
    myqueue = deque([])
    copy = s.replace('x', '')
    if copy != copy[::-1]:
        print(-1)
        continue

    for i in s:
        if i == 'x':
            myqueue.append(i)





