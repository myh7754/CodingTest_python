import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
n , m= map(int, input().split())

a = list(map(int, input().split()))
a.sort()
isused = [False]*(n+1)
arr = []
s = set()
def func():
    if len(arr) == m:
        s.add(tuple(arr))
        return

    for i in range(0, n):
        if not isused[i]:
            if not arr or arr[-1] <= a[i]:
                isused[i] = True
                arr.append(a[i])
                func()
                arr.pop()
                isused[i] = False


func()

for i in sorted(s):
    print(*i)