
n = int(input())
for _ in range(n):
    cmd = list(map(int, input().split()))
    l = []
    for i in range(1,cmd[0]+1):
        l.append(cmd[i])
    avg = sum(l)/cmd[0]
    count = 0
    for i in l:
        if i > avg:
            count+=1
    answer = round(count/cmd[0]*100,3)

    print(f'{answer:.3f}%')