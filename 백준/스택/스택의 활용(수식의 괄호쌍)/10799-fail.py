# 실버2
# 쇠막대기

import sys
input = sys.stdin.readline

n = int(input().rstrip())

stack = []

for word in n:
    if word == '(':
        stack.append(word)
    elif word == ')':
