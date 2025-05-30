while True:
    cmd = list(map(int,input().split()))

    if cmd[0] == 0:
        break
    k = cmd[0]
    s = cmd[1:]
    isused = [False] *len(s)
    arr = []
    def func(start):
        if len(arr) == 6:
            print(*arr)
            return

        for i in range(start, k):
            if not isused[i]:
                isused[i] = True
                arr.append(s[i])
                func(i+1)
                arr.pop()
                isused[i] = False

    func(0)
    print()