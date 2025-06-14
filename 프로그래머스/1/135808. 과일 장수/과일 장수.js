function solution(k, m, score) {
    answer =  0;
    score.sort((a,b) => b-a)
    
    for(i=m-1; i< score.length; i+=m) {
        val = score[i]
        answer += val*m
    }


    return answer;
}