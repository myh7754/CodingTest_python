from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]


def create(c_graph, target):
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= target:
                c_graph[i][j] = 1

def bfs(y,x, graph):
    myque = deque()
    myque.append((y,x))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    graph[y][x] = 1
    count = 1
    while myque:
        y, x = myque.popleft()
        for i in range(4):
            nx = dx[i] +x
            ny = dy[i] +y
            if 0<=nx<n and 0<=ny<n:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    myque.append((ny,nx))
                    count +=1
    return count
m = 0
mh = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] >mh:
            mh = graph[i][j]
for i in range(0,mh):
    c_graph = [[0]*n for _ in range(n)]
    result = []
    create(c_graph,i)
    for j in range(n):
        for k in range(n):
            if c_graph[j][k] == 0:
                result.append(bfs(j,k,c_graph))
    l = len(result)
    m = max(m,l)
    

print(m)
