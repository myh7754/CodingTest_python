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

graph = [
    [],
    [3,8,2]
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
bfs(graph, 1)

