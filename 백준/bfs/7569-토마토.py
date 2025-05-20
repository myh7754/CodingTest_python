#골드5
#토마토

import sys
input = sys.stdin.readline
from collections import deque
m,n,h = map(int, input().rstrip().split())

graph = []

# graph[z][y][x]
for z in range(h):
    layer = []
    for y in range(n):
        layer.append(list(map(int, input().split())))
    graph.append(layer)

start = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                start.append((z,y,x))

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
count = 0
while start:
    z,y,x = start.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx <0 or ny <0 or nz <0 or nx>=m or ny>= n or nz>=h :
            continue
        if graph[nz][ny][nx] == -1:
            continue
        if graph[nz][ny][nx] == 0:
            start.append((nz,ny,nx))
            graph[nz][ny][nx] = graph[z][y][x] +1
            count =graph[nz][ny][nx]

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 0:
                print(-1)
                sys.exit(0)
count = max(count-1, 0)
print(count)
