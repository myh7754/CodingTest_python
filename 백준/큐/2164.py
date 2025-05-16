# 실버4
# 카드2

import sys
from collections import deque
input = sys.stdin.readline
a= deque()
n = int(input())

for i in range(1,n+1):
    a.append(i)

while len(a) != 1:
    a.popleft()
    a.append(a.popleft())

print(a[0])