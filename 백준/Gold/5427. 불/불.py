from collections import deque

t = int(input())

for _ in range(t):
    gx, gy = map(int, input().split())
    graph = [list(input()) for _ in range(gy)]
    s_graph = [[-1]*gx for _ in range(gy)]
    f_graph = [[-1]*gx for _ in range(gy)]
    s = deque()
    f = deque()

    for i in range(gy):
        for j in range(gx):
            if graph[i][j] == '@':
                s.append((i,j))
                s_graph[i][j] = 0
            elif graph[i][j] == '*':
                f.append((i,j))
                f_graph[i][j] = 0

    def bfs(myque, v_graph):
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        while myque:
            y, x = myque.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < gy and 0 <= nx < gx:
                    if graph[ny][nx] == '#' or v_graph[ny][nx] != -1:
                        continue
                    v_graph[ny][nx] = v_graph[y][x] + 1
                    myque.append((ny, nx))

    bfs(f, f_graph)
    bfs(s, s_graph)

    answer = float('inf')
    for i in range(gy):
        for j in range(gx):
            if i == 0 or i == gy -1 or j == 0 or j == gx - 1:
                if s_graph[i][j] != -1:
                    if f_graph[i][j] == -1 or s_graph[i][j] < f_graph[i][j]:
                        answer = min(answer, s_graph[i][j] + 1)

    print(answer if answer != float('inf') else "IMPOSSIBLE")

