# 브론즈2
# 에너그램 만들기

from collections import Counter

word1 = input().strip()
word2 = input().strip()

counter1 = Counter(word1)
counter2 = Counter(word2)

count = 0

for char in set(counter1.keys()).union(counter2.keys()):
    count += abs(counter1.get(char,0) - counter2.get(char,0))

print(count)