import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque

n = int(input())

graph = [list(map(int,input().split())) for i in range(n)]

def func()