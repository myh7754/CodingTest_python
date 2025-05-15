# 실버3
# 두수의 합

n = int(input())

a = list(map(int, input().split()))

target = int(input())
arr = {}
answer = 0

for i in a:
    if arr.get(target- i, 0)> 0: # target - 1 in arr 이게 더 좋음
        answer +=1
    else :
        arr[i] = 1

print(answer)


