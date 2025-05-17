# 실버1
# 숨바꼭질
import sys
input =lambda: sys.stdin.readline().rstrip()
from collections import deque

n , k = map(int,input().split())
count = 0
myqueue = deque()
myqueue.append(n)
graph = [-1]*(200000)
graph[n] = 0
while myqueue:
    start = myqueue.popleft()
    dleft = start-1
    dright = start +1
    dteleport = start*2
    count +=1
    if k == start:
        print(graph[k])
        break

    for next in (dleft, dright, dteleport):
        if 0 <= next < 200000 and graph[next] == -1:
            myqueue.append(next)
            graph[next] = graph[start] +1