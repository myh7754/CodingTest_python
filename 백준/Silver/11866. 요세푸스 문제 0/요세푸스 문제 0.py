#실버4
#요세푸스 문제
from collections import deque

n , k = map(int, input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
answer = []
idx = 0
while arr:
    idx = (idx+k-1) % len(arr)
    answer.append(arr.pop(idx))


print(f"<{', '.join(map(str, answer))}>")
