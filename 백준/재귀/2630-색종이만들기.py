# 색종이 만들기
# 실버2

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
graph = [ list(map(int, input().split())) for i in range(n)]
answer = [0]*2
def check(x,y,size):
    first = graph[y][x]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if graph[j][i] != first:
                return False
    answer[graph[y][x]] += 1
    return True
def func(x,y,n):
    if check(x,y,n):
        return
    new_size = n//2

    for i in range(2):
        for j in range(2):
            func(x+i*new_size,y+j*new_size,new_size)

func(0,0,n)
for i in answer:
    print(i)



