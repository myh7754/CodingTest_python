# 기본 템플릿
def fuc(a):
    # 1. 종료조건
    if 종료조건:
        return 결과값

    # 2. 재귀 호출
    return fuc(다음 파라미터)

# 색종이, 쿼드트리, 압축
def solve(x, y, n):
    color = board[x][y]
    same = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if board[i][j] != color:
                same = False
                break
        if not same:
            break

    if same:
        # 원하는 처리 (예: count[color] += 1)
        return
    else:
        half = n // 2
        solve(x, y, half)
        solve(x, y + half, half)
        solve(x + half, y, half)
        solve(x + half, y + half, half)

# 분할 정복 기반 z탐색
    # 유형 : 특정 순서의 좌표 탐색 (nxn) 탐색중 원하는 인덱스 찾기
def z_search(x, y, size):
    global count
    if size == 1:
        if x == r and y == c:
            print(count)
            exit()
        count += 1
        return

    half = size // 2
    if r < x + half:
        if c < y + half:
            z_search(x, y, half)  # 1사분면
        else:
            count += half * half
            z_search(x, y + half, half)  # 2사분면
    else:
        if c < y + half:
            count += 2 * half * half
            z_search(x + half, y, half)  # 3사분면
        else:
            count += 3 * half * half
            z_search(x + half, y + half, half)  # 4사분면

# 하노이탑
    # 재귀 연습의 대표 예시
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    mid = 6 - start - end  # 1+2+3=6, 중간 막대
    hanoi(n - 1, start, mid)
    print(start, end)
    hanoi(n - 1, mid, end)

# 트리 순회 (dfs 전형)
    # 유형: 트리 구조 탐색
def preorder(node):
    if node == '.':
        return
    print(node, end='')         # Root
    preorder(tree[node][0])     # Left
    preorder(tree[node][1])     # Right

# 백트레킹
    # n과 m 시리즈 등
def backtrack(path):
    if len(path) == m:
        print(*path)
        return
    for i in range(1, n + 1):
        if i not in path:  # 조건: 중복 불허
            backtrack(path + [i])

# dfs를 활용한 영역 개수 세기
    # 섬의 개수 , 단지 번호 붙히기 등
def dfs(x, y):
    visited[x][y] = True
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and board[nx][ny] == 1:
                dfs(nx, ny)

# 재귀로 문자열 압축 / 해제(쿼드트리 출력 등)
    # 유형: 문자열 기반 분할
def quad(x, y, n):
    if is_same(x, y, n):
        return str(board[x][y])
    half = n // 2
    return '(' + \
        quad(x, y, half) + \
        quad(x, y + half, half) + \
        quad(x + half, y, half) + \
        quad(x + half, y + half, half) + ')'