from collections import deque
gy, gx = map(int, input().split())

graph = [list(input()) for i in range(gy)]
jihoon_graph = [[-1]*gx for i in range(gy)]
fire_graph = [[-1]*gx for i in range(gy)]

jihoon = deque()
fire = deque()
for i in range(gy):
    for j in range(gx):
        if graph[i][j] == "J":
            jihoon.append((i,j))
            jihoon_graph[i][j] = 0
        elif graph [i][j] == "F":
            fire.append((i,j))
            fire_graph[i][j] = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]

while fire:
    y,x = fire.popleft()
    for i in range(4):
        nx = dx[i] +x
        ny = dy[i] +y
        if 0<=nx< gx and 0<=ny <gy:
            if fire_graph[ny][nx] == -1 and graph[ny][nx] != "#":
                fire_graph[ny][nx] = fire_graph[y][x] + 1
                fire.append((ny,nx))

while jihoon:
    y,x = jihoon.popleft()
    for i in range(4):
        nx = dx[i] +x
        ny = dy[i] +y
        if 0<=nx< gx and 0<=ny <gy:
            if jihoon_graph[ny][nx] == -1 and graph[ny][nx] != "#" :
                jihoon_graph[ny][nx] = jihoon_graph[y][x] + 1
                jihoon.append((ny,nx))
escape = float('inf')
for i in range(gy):
    for j in range(gx):
        if i== 0 or j == 0 or i == gy-1 or j == gx-1:
            if jihoon_graph[i][j] != -1:
                if jihoon_graph[i][j] < fire_graph[i][j] or fire_graph[i][j] ==-1:
                        escape = min(escape, jihoon_graph[i][j]+1)

if escape == float('inf'):
    print("IMPOSSIBLE")
else:
    print(escape)           
         
    