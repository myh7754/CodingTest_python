# 6593
from collections import deque
gy,gx = map(int,input().split())

graph = [list(map(int,input())) for _ in range(gy)]
visited = [[[0]*gx for i in range(gy)] for j in range(2)]     

def bfs(wall, y,x):
    myque = deque()
    myque.append((wall,y,x))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[wall][y][x] = 1
    while myque:
        wall,y,x = myque.popleft()

        if y == gy -1 and x == gx-1:
            return visited[wall][y][x]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<=ny <gy and 0<=nx<gx:
                if graph[ny][nx] == 0 and visited[wall][ny][nx] == 0:
                    visited[wall][ny][nx] = visited[wall][y][x] + 1
                    myque.append((wall,ny,nx))
                elif graph[ny][nx] == 1 and visited[wall][ny][nx] == 0 and wall == 0:
                    visited[1][ny][nx] = visited[wall][y][x] + 1
                    myque.append((1,ny,nx))
    return -1

print(bfs(0,0,0))
            
            
            

