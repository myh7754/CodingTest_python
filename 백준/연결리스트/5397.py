# 실버2
# 키로커
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    l_stack = list(input().rstrip())
    r_stack = []
    for i in l_stack:
        if i == '<':
            if l_stack:
                r_stack.append(l_stack.pop())
        elif i == '>':
            if r_stack:
                l_stack.append(r_stack.pop())
        elif i == '-':
            if l_stack:
                l_stack.pop()
        else :
            l_stack.append(i)
    print(''.join(l_stack)+''.join(r_stack[::-1]))