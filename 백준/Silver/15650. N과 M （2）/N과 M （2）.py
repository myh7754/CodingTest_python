#실버3
#n과m

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
n , m= map(int, input().split())
isused = [False]*(n+1)
arr = []

def func(start):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(start,n+1):
        if not isused[i]:
            isused[i] = True
            arr.append(i)
            func(i+1)
            arr.pop()
            isused[i] = False

func(1)