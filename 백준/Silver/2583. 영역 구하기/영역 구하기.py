from collections import deque

gy, gx, k = map(int,input().split())
graph = [[0]*gx for i in range(gy)]

for i in range(k):
    sx,sy, ex,ey = map(int,input().split())
    for i in range(sy,ey):
        for j in range(sx,ex):
            graph[i][j] = 1

def bfs(y,x):
    myque = deque()
    myque.append((y,x))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count = 1
    while myque:
        y,x = myque.popleft()
        for i in range(4):
            nx = dx[i] +x
            ny = dy[i] +y
            if 0<=nx<gx and 0<=ny<gy:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    myque.append((ny,nx))
                    count +=1
    return count
result = []
for i in range(gy):
    for j in range(gx):
        if graph[i][j] == 0:
            graph[i][j] = 1
            result.append(bfs(i,j))

print(len(result))
print(*sorted(result))


        
            
            
            