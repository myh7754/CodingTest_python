
t = int(input())


for test in range(1,t+1):
    n,l = map(int,input().split())
    dic = {}
    for i in range(n):
        num, cal = map(int,input().split())
        dic[num] = cal

    # 만약 최대 횟수 혹은 최대 칼로리를 넘는 다면 k를 표시
    num_case = 0
    def func(k, count):
        if count > l or k>n:
            return k
        # 나오는 칼로리
        cal = dic[k]
        count +=1


