# 실버4
# 요세푸스
import sys
input = sys.stdin.readline()
from collections import deque

n , k = map(int , input.rstrip().split())
a = []
result = []
cur = 0
for i in range(1,n+1):
    a.append(i)

for i in range(n):
    cur = (cur+k -1) % len(a)
    result.append(str(a.pop(cur)))

print("<"+', '.join(result) + ">")