from collections import deque

n,m = map(int,input().split())

graph = [list(map(int,input())) for i in range(n)]

def bfs(gy,gx):
    myqueue = deque()
    myqueue.append((gx,gy))
    dx = [ -1, 1, 0, 0]
    dy = [ 0, 0, 1, -1]
    while myqueue:
        x,y = myqueue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<m and 0<=ny<n:
                if graph[ny][nx] == 0:
                    continue
                if graph[ny][nx] == 1:
                    graph[ny][nx] = graph[y][x]+1
                    myqueue.append((nx,ny))

    return graph[n-1][m-1]
print(bfs(0,0))
