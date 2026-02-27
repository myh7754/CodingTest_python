class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int maxW = 0; // 큰 변들 중 최대
        int maxH = 0; // 작은 변들 중 최대
         for (int[] s : sizes) {
            int wit = s[0];
            int hei = s[1];
            
            int big = Math.max(wit,hei);
            int small = Math.min(wit,hei);
             
            maxW = Math.max(big, maxW);
            maxH = Math.max(small, maxH);
            
         }
        return maxH*maxW;
    }
}