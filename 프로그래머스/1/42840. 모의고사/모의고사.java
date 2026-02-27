import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] a = {1,2,3,4,5};
        int[] b = {2,1,2,3,2,4,2,5};
        int[] c = {3,3,1,1,2,2,4,4,5,5};

        int acnt = 0, bcnt = 0, ccnt = 0;

        for (int i = 0; i < answers.length; i++) {  // answers.length
            int ans = answers[i];
            int aidx = i % a.length;                // a.length
            int bidx = i % b.length;
            int cidx = i % c.length;

            if (ans == a[aidx]) acnt++;
            if (ans == b[bidx]) bcnt++;
            if (ans == c[cidx]) ccnt++;
        }

        int max = Math.max(acnt, Math.max(bcnt, ccnt));

        List<Integer> list = new ArrayList<>();
        if (acnt == max) list.add(1);
        if (bcnt == max) list.add(2);
        if (ccnt == max) list.add(3);

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }

        return answer;
    }
}