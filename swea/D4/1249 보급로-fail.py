# 보급로
# D4
from collections import deque
import sys



T = int(input())
for test in range(1,T+1):
    n = int(input())

    graph= [list(map(int, input())) for i in range(n)]
    def bfs(y,x, graph):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        myqueue = deque()
        myqueue.append((y,x))
        visited = [[False]*len(graph) for _ in range(graph[0])]

        while myqueue:
            y,x = myqueue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<= nx < n and 0<= ny <n:
                    if not visited[ny][nx]:
                        graph[ny][nx] = graph[ny][nx]+graph[y][x]
                        myqueue.append((ny,nx))


    print(f'#{test} ')