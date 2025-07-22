import sys
input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
    command = list(input().rstrip())
    l_stack = []
    r_stack = []
    for i in command:
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