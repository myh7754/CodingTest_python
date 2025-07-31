from collections import deque

total, cur, target, u, d = map(int, input().split())

# 층 방문 여부 및 이동 횟수 기록
graph = [0] * (total + 1)

def bfs(start):
    queue = deque()
    queue.append(start)
    graph[start] = 1  # 방문 처리 및 초기값 설정

    while queue:
        current = queue.popleft()

        # 도착하면 출력
        if current == target:
            print(graph[current] - 1)  # 시작을 1로 잡았으므로 -1 해줌
            return

        # 위로
        next_up = current + u
        if u != 0 and next_up <= total and graph[next_up] == 0:
            graph[next_up] = graph[current] + 1
            queue.append(next_up)

        # 아래로
        next_down = current - d
        if d != 0 and next_down >= 1 and graph[next_down] == 0:
            graph[next_down] = graph[current] + 1
            queue.append(next_down)

    # 도착 못한 경우
    print("use the stairs")

bfs(cur)