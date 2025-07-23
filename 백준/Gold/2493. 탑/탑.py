a = int(input())
top = list(map(int, input().split()))

stack = []
result = []

for i in range(a):         # 0번부터 a-1번까지
    current = top[i]

    while stack and stack[-1][1] < current:
        stack.pop()

    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][0])  # 수신자 탑 번호

    stack.append((i + 1, current))   # 번호는 1부터 시작하니까 i+1

print(' '.join(map(str,result)))
