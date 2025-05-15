#브론즈2
#Strfry

n = int(input())

for i in range(n):
    dic = {}
    dic2 = {}
    str1, str2 = map(str, input().split())

    for word in str1:
        dic[word] = dic.get(word,0)+1

    for word in str2:
        dic2[word] = dic2.get(word,0)+1

    if dic == dic2:
        print("Possible")
    else:
        print("Impossible")
