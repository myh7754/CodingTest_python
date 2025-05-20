# 골드3
# 불!

import sys
input =lambda: sys.stdin.readline().rstrip()
from collections import deque

gy ,gx = map(int ,input().split())

graph = [ list(input()) for _ in range(gy)]
fire_graph = [[-1]*gx for _ in range(gy)]
jihoon_graph = [[-1]*gx for _ in range(gy)]
jihoon = deque()
fire = deque()
for y in range(gy):
    for x in range(gx):
        if graph[y][x] == 'J':
            jihoon.append((y,x))
        elif graph[y][x] == 'F':
            fire.append((y,x))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while fire:
    y,x = fire.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if ny < 0 or nx <0 or nx >= gx or ny>=gy:
            continue
        if graph[ny][nx] != '#' and fire_graph[ny][nx] == -1:
            fire_graph[ny][nx] = fire_graph[y][x] +1
            fire.append((ny,nx))

while jihoon:
    y,x = jihoon.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ny < 0 or nx <0 or nx >= gx or ny>=gy:
            print(graph[y][x]+1)
            break

        if graph[ny][nx] != '#' and jihoon_graph[ny][nx] == -1:
            if fire_graph[ny][nx] == -1 or fire[y][x] > jihoon[y][x] +1 :
                jihoon_graph[ny][nx] = jihoon_graph[y][x] +1
                jihoon.append((ny,nx))
