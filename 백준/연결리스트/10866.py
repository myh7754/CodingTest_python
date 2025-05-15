# 덱
# 실버4

import sys
from collections import deque
input = sys.stdin.readline
t = int(input().rstrip())
l_q = deque()
for _ in range(t):
    command = list(map(str, input().rstrip().split()))
    if command[0] == 'push_front':
        l_q.appendleft(command[1])
    elif command[0] == 'push_back':
        l_q.append(command[1])
    elif command[0] == 'pop_front':
        if l_q:
            print(l_q.popleft())
        else :
            print(-1)
    elif command[0] == 'pop_back':
        if l_q:
            print(l_q.pop())
        else :
            print(-1)
    elif command[0] == 'size':
            print(len(l_q))
    elif command[0] == 'empty':
        if l_q:
            print(0)
        else :
            print(1)
    elif command[0] == 'front':
        if l_q:
            print(l_q[0])
        else :
            print(-1)
    elif command[0] == 'back':
        if l_q:
            print(l_q[-1])
        else:
            print(-1)
