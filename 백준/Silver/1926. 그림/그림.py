import sys
input = sys.stdin.readline
from collections import deque

gy, gx = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip().split())) for i in range(gy)]


painting = []
def bfs(x,y):
    myqueue = deque()
    myqueue.append((y,x))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    graph[y][x] = 0
    count = 1
    while myqueue :
        y,x = myqueue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx>= gx or ny < 0 or ny>=gy:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                count+=1
                myqueue.append((ny,nx))
    return count

for y in range(gy):
    for x in range(gx):
        if graph[y][x] == 1:
            painting.append(bfs(x,y))

print(len(painting))
print(max(painting)  if painting else 0)