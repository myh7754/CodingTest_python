import sys
input = sys.stdin.readline
from collections import deque

gy, gx = map(int, input().rstrip().split())

graph = [list(map(int, input().rstrip())) for _ in range(gy)]

def bfs(x,y):
    myqueue = deque()
    myqueue.append((y,x))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while myqueue:
        y,x = myqueue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny<0 or nx>=gx or ny>=gy:
                continue

            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                myqueue.append((ny,nx))
                graph[ny][nx] = graph[y][x] +1
    return graph[gy-1][gx-1]

print(bfs(0,0))
