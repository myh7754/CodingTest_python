import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
n , m= map(int, input().split())

a = list(map(int, input().split()))
a.sort()
isused = [False]*(n+1)
arr = []
def func():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(0, n):
        arr.append(a[i])
        func()
        arr.pop()



func()

