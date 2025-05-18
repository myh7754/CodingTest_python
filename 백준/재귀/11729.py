# 골드5
# 하노이탑 이동순서

import sys
input =lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**5)  # 충분히 큰 수로 설정
from collections import deque

# n-1
# n
# n-1을 옮길 수 있으면 n을 옮길 수 있다.
k = int(input())
# a로 출발 , b 도착, c 현재값
count = 0
def func(a,b,n): # a번 기둥에서 b번 기둥으로 n을 옮기는 방법을 출력하는 함수 1, 3
    # base condition
    global count
    if n == 1:
        print(a , b)
        return
    # 6-a-b : 출발지도 도착지도 아닌 기둥의 번호
    func(a ,6-a-b ,n-1)
    print(a, b)
    func(6-a-b, b ,n-1)
print(2**k-1)
func(1,3,k)
