# 실버4
# 균형잡힌 세상

import sys
input = sys.stdin.readline

a = ''
while True:
    statck = []
    a = input().rstrip()
    if a == '.':
        break
    answer =''
    for word in a:
        if word == "(" or word == "[":
            statck.append(word)
        elif word == ")" :
            if statck and statck[-1] == "(":
                statck.pop()
            else:
                if len(statck) == 0:
                    statck.append(word)
                break
        elif word == "]" :
            if statck and statck[-1] == "[":
                statck.pop()
            else:
                if len(statck) == 0:
                    statck.append(word)
                break
    if statck:
        answer = "no"
    else :
        answer = "yes"
    print(answer)