# 평행사변형
# D3

import sys
sys.stdin = open("../input/1_input_sample.txt", "r")
input =lambda : sys.stdin.readline().rstrip()
from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    answer = n*n
    print(f'{test_case} {answer}')
