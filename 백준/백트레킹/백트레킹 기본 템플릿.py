
import sys
input =lambda : sys.stdin.readline().rstrip()
from collections import deque

# 백트레킹:  N과 M , N-Queen

# 기본 템플릿
def backtrack(현재상태):
    if 종료조건:
        결과처리
        return

    for 선택지 in 가능한선택지들:
        if 선택지 사용 가능:
            상태변경(선택)
            backtrack(변경된 상태)
            상태복구(선택 취소)
