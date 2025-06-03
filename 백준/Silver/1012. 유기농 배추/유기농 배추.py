import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
n = int(input())

def bfs(y,x):
    myqueue = deque()
    myqueue.append((y,x))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count =1
    while myqueue:
        y,x = myqueue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx <gx and 0<= ny < gy:
                if graph[ny][nx] == 0:
                    continue
                if graph[ny][nx] == 1:
                    myqueue.append((ny,nx))
                    graph[ny][nx] = 0
                    count += 1
    return count


for _ in range(n):
    gx,gy,k = map(int, input().split())

    graph = [[0]*gx for i in range(gy)]
    pating = []
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1


    for i in range(gy):
        for j in range(gx):
            if graph[i][j] == 1:
                pating.append(bfs(i,j))

    print(len(pating))
