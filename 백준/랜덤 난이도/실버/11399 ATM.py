# 실버4
n = int(input())

l = list(map(int, input().split()))
l.sort()

s = 0
ss = 0
for i in l:
    s +=i
    ss +=s
print(ss)


