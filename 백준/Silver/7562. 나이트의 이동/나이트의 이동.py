import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

t = int(input())
def bfs(y,x,graph):
    myqueue = deque()
    myqueue.append((y,x))
    dx = [-2,-2,2,2,-1,-1,1,1]
    dy = [1,-1,1,-1,2,-2,2,-2]
    while myqueue :
        (y,x) = myqueue.popleft()
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]

            if 0<= nx< n and 0<=ny<n:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    myqueue.append((ny,nx))



for i in range(t):
    n = int(input())
    graph = [ [0]*n for _ in range(n)]
    start_y, start_x = map(int, input().split())
    (a_y, a_x) = map(int, input().split())
    if start_y == a_y and start_x == a_x:
        print(0)
        continue
    bfs(start_y,start_x,graph)
    print(graph[a_y][a_x])
