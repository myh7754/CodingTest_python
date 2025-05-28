import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
n , m= map(int, input().split())

arr = []
def func():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if arr and arr[-1] <= i:
            arr.append(i)
            func()
            arr.pop()
        elif len(arr) == 0:
            arr.append(i)
            func()
            arr.pop()


func()


