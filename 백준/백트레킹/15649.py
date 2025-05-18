# N과 M
# 실버3

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
n , m= map(int, input().split())
isused = [False] * (n+1)
arr = [0]*m
def func(k):

    if k == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if not isused[i]:
            isused[i] = True
            arr[k] = i
            func(k+1)
            isused[i]= False
func(0)