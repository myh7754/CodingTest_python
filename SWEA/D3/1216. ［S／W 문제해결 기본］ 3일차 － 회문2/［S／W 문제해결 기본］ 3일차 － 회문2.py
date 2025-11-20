T = 10;

for t in range(1,T+1):
    N = int(input())
    str = [input().strip() for _ in range(100)]

    max_len = 1
    k = 100
    for y in range(k):
        for start in range(k):
            for end in range(start+1, k+1):
                if str[y][start:end] == str[y][start:end][::-1]:
                    max_len = max(max_len, end-start)

    for x in range(k):
        for start in range(k):
            for end in range(start+1, k+1):
                vertical = ''.join(str[row][x] for row in range(start,end))
                if vertical == vertical[::-1]:
                    max_len = max(max_len, end-start)

    result = max_len
    print(f"#{N} {result}")
