# 플레티넘5
# 최솟값 찾기

# 풀기 위한 아이디어 2가지
# 현재 들어오는 값보다 큰 값은 다 지워야한다.
# 인덱스가 넘어간 값을 지워야한다.

import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().rstrip().split())
a = list(map(int, input().split()))
dq = deque()  # 인덱스를 저장할 덱

for i in range(n):

    while dq and a[dq[-1]] >= a[i]:
        dq.pop()

    dq.append(i)

    if dq[0] <= i - l:
        dq.popleft()

    print(a[dq[0]], end=' ')