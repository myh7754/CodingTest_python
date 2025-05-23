from collections import deque

t = int(input())

graph = [[0]*100 for i in range(100)]
for i in range(t):
    n,m = map(int,input().split())
    for i in range(n,n+10):
        for j in range(m,m+10):
            graph[i][j] = 1


def bfs(y, x):
    myqueue = deque()
    myqueue.append((y,x))
    graph[y][x] = 0
    count = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while myqueue:
        y,x = myqueue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= ny <100 and 0<= nx <100:
                if graph[ny][nx] == 0:
                    continue
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    myqueue.append((ny,nx))
                    count +=1
    return count

answer = []
for i in range(100):
    for j in range(100):
        if graph[j][i] == 1:
            answer.append(bfs(j,i))
print(sum(answer))
