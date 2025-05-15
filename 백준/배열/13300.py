# 브론즈2
# 방배정

n , k = map(int, input().split())
dic1 = {}
dic2 = {}
answer = 0
for i in range(n):
    gen, grade = map(int, input().split())
    if gen == 0:
        dic1[grade] = dic1.get(grade, 0)+1
    else :
        dic2[grade] = dic2.get(grade, 0)+1


for i in range(1,7):
    answer += (dic1.get(i, 0) + k - 1) // k
    answer += (dic2.get(i, 0) + k - 1) // k
print(answer)
