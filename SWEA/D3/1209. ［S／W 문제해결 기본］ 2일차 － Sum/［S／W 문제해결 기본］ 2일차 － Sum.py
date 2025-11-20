T = 10;

for t in range(1,T+1):
    N = int(input())
    graph =[list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    for x in range(100):
        max_sum = max(max_sum, sum(graph[x]))
    #
    for y in range(100):
        col_max = 0
        for x in range(100):
            col_max += graph[x][y]
        max_sum = max(max_sum, col_max)

    diag1 = 0
    diag2 = 0
    for y in range(100):
        diag1 += graph[y][y]
        diag2 += graph[y][99-y]
    max_sum = max(diag1,diag2,max_sum)

    print(f"#{t} {max_sum}")