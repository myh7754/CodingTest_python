# 실버4
# 큐
import sys
from collections import deque
input = sys.stdin.readline
a= deque()
n = int(input())

for _ in range(n):
    cmd = list(map(str, input().rstrip().split()))

    if cmd[0] == "push":
        a.append(cmd[1])
    elif cmd[0] =="pop":
        print(a.popleft() if a else -1)
    elif cmd[0] =="size":
        print(len(a))
    elif cmd[0] =="empty":
        print(0 if a else 1)
    elif cmd[0] =="front":
        print(a[0] if a else -1)
    elif cmd[0] =="back":
        print(a[-1] if a else -1)
