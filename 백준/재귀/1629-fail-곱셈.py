# 실버1
# 곱셈

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque

A,B,C = map(int, input().split())

def func(a,b,c):
    if b == 1:
        return a % c

    half = func(a, b//2, c)
    print(half)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


print(func(A,B,C))
