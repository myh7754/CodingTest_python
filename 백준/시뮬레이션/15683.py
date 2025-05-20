import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque
gy,gx  = map(int,input().split())
graph = [list(map(int, input().split())) for i in range(y)]



for i in range(gy):
    for j in range(gx):
        if graph[i][j] == 5:


# 단순 방향 직진
def bfs(n,graph,x,y):
    if n == 5:
        # 4방향 (상, 하, 좌, 우)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            while 0 <= nx < gx and 0<= ny < gy:
                if graph[ny][nx] == 6:
                    break
                if graph[ny][nx] == 0:
                    graph[ny][nx] = '#'
                ny += dy
                nx += dx
    if n ==
