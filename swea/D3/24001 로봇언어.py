# 로봇언어
# D3

T = int(input())
for test_case in range(1, T + 1):
        n = list(input())

        l_list = []
        r_list = []
        left_list = []
        right_list = []
        for i in n:
            if i == '?':
                l_list.append('L')
                r_list.append('R')
            else :
                l_list.append(i)
                r_list.append(i)

        cur_l = 0
        cur_r = 0
        for i in l_list:
            if i == 'L':
                cur_l -=1
                left_list.append(cur_l)
            elif i == 'R':
                cur_l +=1
                left_list.append(cur_l)

        for i in r_list:
            if i == 'L':
                cur_r -= 1
                right_list.append(cur_r)
            elif i == 'R':
                cur_r += 1
                right_list.append(cur_r)

        answer = max(abs(min(left_list)), max(right_list))

        print(f'{answer}')