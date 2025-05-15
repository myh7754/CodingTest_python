# 브론즈2
# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

result = a*b*c
dic= {}
for word in str(result):
    dic[word] = dic.get(word,0)+1

for i in range(0,10):
    print(dic.get(str(i),0))