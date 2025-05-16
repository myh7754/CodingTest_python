# 실버2
# 스택 수열

import sys
input = sys.stdin.readline

n = int(input())
a = []
cnt = 1
for _ in range(n):
    k = int(input())
    while k != cnt:
        a.append(cnt)
        cnt+=1



