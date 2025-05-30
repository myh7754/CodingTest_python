n = int(input())



isused = [False]*n #행
disig1 = set() # 대각1
disig2 = set() # 대각2
count = 0
def func(c):
    global count
    if c == n:
        count +=1
        return

    for i in range(n):
        if isused[i] == False and (c-i)  not in disig1 and (i+c) not in disig2:
            isused[i] = True
            disig1.add(c-i)
            disig2.add(c+i)
            func(c+1)
            isused[i] = False
            disig1.remove(c-i)
            disig2.remove(c+i)
func(0)
print(count)

