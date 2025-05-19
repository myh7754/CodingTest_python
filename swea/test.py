# import sys

#
# T = 10
#
# print(2^2)
import sys
input =lambda : sys.stdin.readline().rstrip()
sys.stdin = open("input/input (3).txt", "r")
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    n,m = map(int, input().split())
    graph = []
    for i in str(n):
        graph.append(int(i))

    for i in range(m):