# 지명선수
# d3
from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    player = set(range(1,n+1))

    a = deque(map(int, input().split()))
    a_team = []
    b = deque(map(int, input().split()))
    b_team = []
    i = 0
    while player:
        while a:
            a_player = a.popleft()
            if a_player in player:
                a_team.append(a_player)
                player.remove(a_player)
                break
        while b:
            b_player = b.popleft()
            if b_player in player:
                b_team.append(b_player)
                player.remove(b_player)
                break

    result = []
    for i in range(1,n+1):
        if i in a_team:
            result.append('A')
        else :
            result.append('B')

    print(*result)
