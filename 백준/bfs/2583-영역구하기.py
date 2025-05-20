
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

graph_y,graph_x,k = map(int, input().split())

graph = [[0]*(graph_x) for i in range(graph_y)]

for _ in range(k):
    x_1,y_1, gx,gy = map(int,input().split())
    for i in range(y_1, gy):
        for j in range(x_1,gx):
            graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    graph[y][x] = 1
    count = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<graph_x and 0<=ny<graph_y:
                if graph[ny][nx] == 1:
                    continue
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    queue.append((ny,nx))
                    count += 1
    return count
answer = []
for i in range(graph_y):
    for j in range(graph_x):
        if graph[i][j] == 0:
            answer.append(bfs(i,j))
print(len(answer))
print(*sorted(answer))


