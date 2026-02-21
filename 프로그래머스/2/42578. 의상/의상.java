import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> cnt = new HashMap<>();

        // 1) 종류별 개수 세기
        for (String[] c : clothes) {
            String type = c[1];
            cnt.put(type, cnt.getOrDefault(type, 0) + 1);
        }

        // 2) (개수 + 1) 전부 곱하기
        int ans = 1;
        for (int n : cnt.values()) {
            ans *= (n + 1);
        }

        // 3) 전부 안 입는 경우 1개 빼기
        return ans - 1;
    }
}