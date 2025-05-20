# 계단오르기
# 실버3

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
t = int(input())
stairs = []
dp = [0]*(t+1) # i번째 계단의 올라갔을 때 정수합의 최대값
for i in range(t):
    stairs.append(int(input()))
    if i == 0 :
        dp[0] = stairs[0]

dp[i]




