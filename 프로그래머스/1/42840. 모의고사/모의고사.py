def solution(answers):
    re = []
    def sol1(answers):
        a1 = [1,2,3,4,5]
        idx = 0
        count = 0
        for i in answers:
            if i == a1[idx%5]:
                count+=1
            idx+=1
        return count
    def sol2(answers):
        a2 = [2,1,2,3,2,4,2,5]
        idx = 0
        count =0
        for i in answers:
            if i == a2[idx%8]:
                count +=1
            idx +=1
        return count
    def sol3(answers):
        a2 = [3,3,1,1,2,2,4,4,5,5]
        idx = 0
        count =0
        for i in answers:
            if i == a2[idx%10]:
                count +=1
            idx +=1
        return count
    dic = {1 : sol1(answers) , 2 : sol2(answers) , 3 : sol3(answers)}
    max_dic = max(dic.values())
    for key ,value in dic.items():
        if value == max_dic:
            re.append(key)
    return re
