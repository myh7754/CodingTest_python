n, m = map(int ,input().split())

a = list(map(int, input().split()))
isused = [False]*n
count = 0
arr = []
cnt = 0
def func(start):
    global cnt
    if len(arr) == n :
        return

    for i in range(start , n):
        if not isused[i]:
            isused[i] = True
            arr.append(a[i])
            if sum(arr) == m:
                cnt +=1
            func(i+1)
            arr.pop()
            isused[i] = False

func(0)
print(cnt)