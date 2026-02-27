import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> cnt = new HashMap<>();
        int i = 1;
        for (String[] c : clothes) {
            cnt.put(c[1], cnt.getOrDefault(c[1],0) +1);
            
        }
        for (int k : cnt.values()) {
            i = i*(1+k);
        }
        return i-1;
    }
}