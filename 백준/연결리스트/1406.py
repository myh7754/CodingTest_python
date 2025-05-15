# 실버2
# 에디터

import sys
input = sys.stdin.readline

l_stack = list(input().strip())
r_stack = []
cursor = len(l_stack)

n = int(input())
for _ in range(n):
    cmd = list(map(str, input().split()))
    if cmd[0] == "L":
        if l_stack:
            r_stack.append(l_stack.pop())
    elif cmd[0] =="D":
        if r_stack:
            l_stack.append(r_stack.pop())
    elif cmd[0] =="B":
        if l_stack:
            l_stack.pop()
    elif cmd[0] =="P":
        l_stack.append(cmd[1])

print(''.join(l_stack)+''.join(r_stack[::-1]))