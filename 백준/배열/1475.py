# 실버5
# 방번호

n = str(input())
dic = {}
for word in n:
    if word == '6' or word =='9':
        word = '6'
    dic[word] = dic.get(word, 0)+1

mx = 0
for i in range(0,9):
    if i == 6 and dic.get(str(i),0) > 1 :
        dic[str(i)] = dic[str(i)]/2 + dic[str(i)]%2

    if mx < dic.get(str(i),0):
        mx = dic.get(str(i),0)

print(int(mx))

