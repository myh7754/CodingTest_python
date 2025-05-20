# 색종이 만들기
# 실버2

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque

n = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]


def func(n):


