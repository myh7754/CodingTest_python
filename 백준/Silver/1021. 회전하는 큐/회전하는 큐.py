import sys
from collections import deque
input = sys.stdin.readline
a = deque()

n , m =map(int, input().rstrip().split())

for i in range(1,n+1):
    a.append(i)

t = list(map(int, input().rstrip().split()))
answer = 0
for i in t:
    l = len(a)
    midl = l//2
    idx = a.index(i)

    cmd = "L" if midl >= idx else "R"
    while True:
        if cmd == "L":
            if i == a[0]:
                a.popleft()
                break
            else :
                a.rotate(-1)
                answer +=1
        elif cmd == "R":
            if i == a[0]:
                a.popleft()
                break
            else :
                a.rotate(1)
                answer += 1




print(answer)