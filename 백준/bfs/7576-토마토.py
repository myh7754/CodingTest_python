# 골드5
# 토마토

import sys
input = sys.stdin.readline
from collections import deque

gx, gy = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for _ in range(gy)]
start = deque()
myqueue = deque()
for y in range(gy):
    for x in range(gx):
        if graph[y][x] == 1:
            myqueue.append((y, x))
count = 0


dx = [-1,1,0,0]
dy = [0,0,-1,1]
while myqueue:
    y,x = myqueue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny<0 or nx>=gx or ny>=gy:
            continue
        if graph[ny][nx] >= 1:
            continue
        if graph[ny][nx] == 0:
            myqueue.append((ny,nx))
            graph[ny][nx] = graph[y][x]+1
            count =graph[ny][nx]

for y in range(gy):
    for x in range(gx):
        if graph[y][x] == 0:
            print(-1)
            sys.exit(0)
count = max(count-1, 0)
print(count)


