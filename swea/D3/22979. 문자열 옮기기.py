from collections import deque

n = int(input())
for i in range(n):
    s = deque(input())
    c_num = int(input())
    cmd = list(map(int, input().split()))
    cmd = sum(cmd)

    if i > 0:
        cmd = cmd % len(s)
        for i in range(cmd):
            s.append(s.popleft())
    if i < 0:
        cmd = cmd % len(s)
        for i in range(abs(cmd)):
            s.appendleft(s.pop())
    print(''.join(s))
