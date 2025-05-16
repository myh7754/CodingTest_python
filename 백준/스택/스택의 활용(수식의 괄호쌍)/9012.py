#실버4
#괄호

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    w = input().rstrip()
    stack = []
    answer = ''
    for word in w:

        if word  == '(' :
            stack.append(word)
        elif word == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else :
                stack.append("0")
                break
    if stack:
        answer = "NO"
    else:
        answer = "YES"

    print(answer)

