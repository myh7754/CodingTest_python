# 골드5
# AC
import sys, json
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    vector = 'L'
    p = input().rstrip()
    n = int(input())
    k = json.loads(input().rstrip())
    a = deque(k)
    answer= ''
    for cmd in p:
        if cmd == "R":
            if vector == 'R':
                vector = 'L'
            else:
                vector = 'R'
        elif cmd == "D":
            if a and vector == 'L':
                a.popleft()
            elif a and vector == 'R':
                a.pop()
            else :
                answer = "error"
                break

    if answer != "error":
        if vector == 'R':
            a.reverse()
        answer = json.dumps(list(a))
        print(answer.replace(' ', ''))
    else :
        print(answer)