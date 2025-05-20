import sys
아스키 코드
a = 97 ~ z = 122
A = 65 ~ Z = 90

입출력
"hello"
input().strip() # strip은 양쪽 앞 뒤 끝에 있는 공백 및 enter 문자를 제거 합니다.
input().rstrip() # 오른쪽 끝에 있는 공백 및 enter 만 제거
input = sys.stdin.readline
input() # "hello \n" readline으로 선언한 input은 enter까지 그대로 읽음
input().rstrip() # 그렇기 때문에 rstrip으로 개행 및 공백 제거 필수 s = "hello"
# 만약 개행(enter)는 지우고 공백은 필요한 경우
line = input().rstrip('\n')  # "hello "
list(input) # "hello"를 입력했다면 ['h','e','l','l','o']가 됨

딕셔너리
dic = {"1" : "3", "2": "2"}
value = dic.get("1", 0) # 찾고 싶은 key, 만약 값이 없다면 0
print(value)
value = min(dic, key=dic.get) # 딕셔너리의 값중 작은 값 찾기
print(value)
# 기본값이 0으로 들어있는 딕셔너리
from collections import defaultdict
d = defaultdict(int)
dic['a'] +=1
dic['b'] +=2
print(dic)  # {'a': 1, 'b': 2}

덱
from collections import deque
dq = deque()
dq2 = deque([1,2,3])
dq2.extend([4,5,6])
# deque([1,2,3,4,5,6])
dq2.extend('abc')
# deque([1,2,3,4,5,6,'a','b','c'])
dq2.extendleft([7,8,9])
# deque([9,8,7,1,2,3,4,5,6,'a','b','c'])

dq = deque([1,2,3,4,5])
dq.rotate(2) # 오른쪽으로 2칸이동
# dq = [4,5,1,2,3]
dq.rotate(-3) # 왼쪽으로 3간이동
# dq = [2,3,4,5,1]
# deque


list 혹은 deque가 있다면
cur = 10
charge= [5, 12, 13, 16, 18]
trueidx = [cur < x < cur+5 for x in charge] # cur 값과 cur+5 값 사이에 있다면 true, 없다면 false
# => trueidx = [False, True, True, False, False]
범위 내의 최대 idx = 컬렉션의 수 -1 - trueidx[::-1].index(True) # 위 trueidx에서 구해진 최대 index값 찾기
list.insert(index, value) : index에 value 삽입

셋(set)
set1 & set2 : 교집합
set1 - set2 : 차집합
set1 | set2 : 합집합

json 파서
import json
어떤 문자열 데이터를 객체로 바꿔주거나 문자로 바꿔줌
'[ 1, 2, 3, 4]' 이러한 문자열 값을 배열로 바꾸고 싶다면
jsonStr = json.loads('[ 1, 2, 3, 4]') # 이러면 jsonStr은 배열로 바뀜
역으로 배열을 문자열로 바꾸고 싶다면
jsonStr = [1,2,3,4]
Dump = json.dumps(jsonStr) # 이러면 Dump는 '[1, 2, 3, 4]' 이러한 문자열로 바뀜

bfs 암기
from collections import deque
graph = []
def bfs(start, graph):
    visited = [False]* len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

dfs
# 재귀방식
def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

# 스택방식
def dfs(start, graph):
    visited = [False] * len(graph)
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in reversed(graph[node]):  # 순서 조정 필요시 reverse
                if not visited[neighbor]:
                    stack.append(neighbor)

# math 수학계산할 때 자주사용
import math
math.gcd(a,b) # a, b의 최대공약수
math.lcm(a,b) # a, b의 최소 공배수
math.factorial(n) # 팩토리얼

print(math.ceil(2.3))   # 3 (올림)
print(math.floor(2.7))  # 2 (내림)
print(math.sqrt(16))    # 4.0 (제곱근)

# 조합 및 순열
from itertools import combinations, permutations # 조합, 순열
arr = [1, 2, 3]

print(list(combinations(arr, 2)))  # n개 중 r개를 순서 없이 뽑기
# → [(1, 2), (1, 3), (2, 3)]

print(list(permutations(arr, 2))) # n개 중 r개를 순서 있게 뽑기
# → [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]


#우선순위큐 heapq

# 이진탐색 bisect

#


