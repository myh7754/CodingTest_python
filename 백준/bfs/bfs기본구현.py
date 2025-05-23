import sys
input = sys.stdin.readline
from collections import deque
# bfs 문제 종류
# 최단거리 , 상태 전이(전파, 감염 등), (그룹개수 세기), (퍼즐 및 상태 탐색), (벽부수고 이동), (다차원 , 3D bfs) , 최소 횟수로 원하는 상태 만들기


# 기본구조
def bfs(graph, start):
    visited = [False]*len(graph)
    myqueue = deque([start])
    visited[start] = True
    while myqueue:
        node = myqueue.popleft()
        for neighbor in myqueue[node]:
            if not visited[neighbor] :
                visited[neighbor] = True
                myqueue.append(neighbor)

# visited를 사용하는 이유
# 원본 그래프를 유지하고 싶을 때
# 데이터와 구분된 방문 기록을 관리하고 싶을 때



## bfs의 영역 수와 영역의 개수를 구하는 템플릿
import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

graph_y,graph_x,k = map(int, input().split())

graph = [[0]*(graph_x) for i in range(graph_y)]

for _ in range(k):
    x_1,y_1, gx,gy = map(int,input().split())
    for i in range(y_1, gy):
        for j in range(x_1,gx):
            graph[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    graph[y][x] = 1
    count = 1
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<graph_x and 0<=ny<graph_y:
                if graph[ny][nx] == 1:
                    continue
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    queue.append((ny,nx))
                    count+=1
    return count
answer = []
for i in range(graph_y):
    for j in range(graph_x):
        if graph[i][j] == 0:
            answer.append(bfs(i,j))

# 결과 출력
print(len(answer))
print(max(answer)  if answer else 0)
