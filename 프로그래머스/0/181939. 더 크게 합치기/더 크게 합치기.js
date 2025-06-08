function solution(a, b) {
    var answer = 0;
    na = String(a) + String(b)
    nb = String(b) + String(a)
    answer = na > nb ? String(a) + String(b) : String(b) + String(a);
    
    return Number(answer);
}