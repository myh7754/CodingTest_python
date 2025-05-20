# 1,2,3 더하기
# 실버3

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
t = int(input())

for _ in range(t):
    n = int(input())
    # n이 작을 경우에만 미리 리턴
    if n == 1:
        print(1)
        continue
    elif n == 2:
        print(2)
        continue
    elif n == 3:
        print(4)
        continue
    dp = [0]*(15)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if n < 4:
        print(dp[n])
        break
    for k in range(4,n+1):
        dp[k] = dp[k-1] + dp[k-2] + dp[k-3]

    print(dp[n])