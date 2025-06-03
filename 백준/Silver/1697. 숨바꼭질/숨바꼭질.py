from collections import deque

n,k = map(int,input().split())

graph = [0]*100001

def bfs(cur):
    myqueue = deque()
    myqueue.append(cur)

    while myqueue:
        cur = myqueue.popleft()
        if cur == k:
            print(graph[cur])
            break
        dx1 = cur+1
        dx2 = cur-1
        dx3 = cur*2
        if 0<= dx1 <= 100000:
            if graph[dx1] == 0:
                graph[dx1] = graph[cur] +1
                myqueue.append(dx1)
        if 0<= dx2 <= 100000:
            if graph[dx2] == 0:
                graph[dx2] = graph[cur] +1
                myqueue.append(dx2)
        if 0<= dx3 <= 100000:
            if graph[dx3] == 0:
                graph[dx3] = graph[cur] +1
                myqueue.append(dx3)

bfs(n)