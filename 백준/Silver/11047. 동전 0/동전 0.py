
n , k = map(int, input().split())

coin = []
for i in range(n):
    num = int(input())
    coin.append(num)


coin.sort(reverse=True)
count = 0
for coin in coin:
    if coin <= k:
        count += k//coin
        k %= coin

print(count)

