# 색상환
# D3

import sys

T = int(input())

for _ in range(T):
    n, m = map(str, input().split())
    graph = ['red', 'orange','yello','green','blue','purple']

    nidx = graph.index(n)
    midx = graph.index(m)
    c = abs(nidx - midx)
    if nidx == midx:
        print('E')
    elif (nidx+3)%len(graph) == midx:
        print('C')
    elif c == 1 or c == 5:
        print('A')
    else:
        print('X')
