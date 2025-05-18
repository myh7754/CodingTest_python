# 골드5
# 적록색약

import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque

n = int(input())

graph = [list(input()) for _ in range(n)]
r_graph = [['']*n for _ in range(n)]
answer1 = []
answer2 = []

for y in range(n):
    for x in range(n):
        if graph[y][x] == "G":
            r_graph[y][x] = 'R'
        else :
            r_graph[y][x] = graph[y][x]

# 일반 bfs
def bfs(y,x, graph):
    myqueue = deque()
    myqueue.append((y,x))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count = 1
    color = graph[y][x]
    graph[y][x] = '0'
    while myqueue:
        y,x = myqueue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n:
                if graph[ny][nx] == '0':
                    continue
                if graph[ny][nx] == color:
                    graph[ny][nx] = '0'
                    myqueue.append((ny,nx))
                    count +=1
    return count

for y in range(n):
    for x in range(n):
        if graph[y][x] != '0':
            answer1.append(bfs(y,x,graph))

        if r_graph[y][x] != '0':
            answer2.append(bfs(y, x, r_graph))

print(len(answer1) , len(answer2))


