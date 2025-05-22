import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque

n, y , x = map(int, input().split())

# def func(n,y,x):
#     if n == 0:
#         return 0
#     half = 2**(n-1)
#     quadrant_size = half * half
#     #1사분면
#     if y < half  and x < half:
#         return func(n-1,y,x)
#     #2사분면
#     elif y < half and x > half:
#         return func(n-1, y,x -half)
#     #3사분면
#     elif y > half and x < half:
#     #4사분면
#     elif y > half and x > half:



