#실버4
#좋은단어

import sys
input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    w = input().rstrip()
    stack = []

    for word in w:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    if len(stack) == 0:
        count+=1
print(count)






