# 실버2
# 종이의개수

import sys
input = lambda : sys.stdin.readline().rstrip()
n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]

answer = [0]*3

def check(x,y,size):
    first = graph[y][x]
    for i in range(y,y + size):
        for j in range(x,x+size):
            if graph[i][j] !=first:
                return False
    return True

def func(x,y,n):
    if check(x,y,n):
        answer[graph[y][x]+1] +=1
        return

    new_size = n//3
    for i in range(3):
        for j in range(3):
            func(x+j*new_size,y+i*new_size,new_size)

func(0,0,n)

for count in answer:
    print(count)
