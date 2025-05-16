# 실버4
# 제로
import sys
input = sys.stdin.readline
n = int(input())
a = []
cursor = 0
for _ in range(n):
    k = int(input())
    if k == 0 and a:
        a.pop()
    else :
        a.append(k)
answer = sum(a)
print(answer)
