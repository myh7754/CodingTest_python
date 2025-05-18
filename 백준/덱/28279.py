# 덱2
# 실버4

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
n = int(input())
myqueue = deque()
for i in range(n):
    cmd = list(map(int , input().split()))
    print(cmd[0])
    if cmd[0] == 1:
        myqueue.appendleft(cmd[1])
    elif cmd[0] == 2:
        myqueue.append(cmd[1])
    elif cmd[0] == 3:
        if myqueue :
            print(myqueue.popleft())
        else :
            print(-1)
    elif cmd[0] == 4:
        if myqueue :
            print(myqueue.pop())
        else :
            print(-1)
    elif cmd[0] == 5:
        print(len(myqueue))
    elif cmd[0] == 6:
        if myqueue :
            print(0)
        else :
            print(1)
    elif cmd[0] == 7:
        if myqueue :
            print(myqueue[0])
        else :
            print(-1)
    elif cmd[0] == 8:
        if myqueue :
            print(myqueue[-1])
        else :
            print(-1)