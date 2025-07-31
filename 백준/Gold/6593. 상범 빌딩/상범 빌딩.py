
# 6593
from collections import deque
while True:
    h,gy,gx = map(int, input().split())
    if h == 0 and gy == 0 and gx == 0:
        break
    graph = []
    for i in range(h):
        layer = []
        for j in range(gy):
            layer.append(list(input()))
        cdd = input()
        graph.append(layer)
    def bfs(z,y,x):
        myque = deque()
        myque.append((z,y,x))
        dx = [-1,1,0,0,0,0]
        dy = [0,0,-1,1,0,0]
        dz = [0,0,0,0,-1,1]
        graph[z][y][x] = 0
        while myque:
            z,y,x = myque.popleft()
            for i in range(6):
                nx = dx[i] +x
                ny = dy[i] +y
                nz = dz[i] +z
                if 0<=nz<h and 0<=ny<gy and 0<=nx<gx:
                    if graph[nz][ny][nx] == '#':
                        continue
                    if graph[nz][ny][nx] == '.':
                        graph[nz][ny][nx] = graph[z][y][x] +1
                        myque.append((nz,ny,nx))
                    if graph[nz][ny][nx] == 'E':
                        return graph[z][y][x] +1
    minute = 'trap'
    for i in range(h):
        for j in range(gy):
            for k in range(gx):
                if graph[i][j][k] == 'S':
                    minute = bfs(i,j,k)

    if minute == None:
        print("Trapped!")
    else :
        print(f'Escaped in {minute} minute(s).')    

