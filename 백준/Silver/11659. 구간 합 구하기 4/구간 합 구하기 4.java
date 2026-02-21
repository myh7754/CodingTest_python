import java.io.*;
import java.util.*;

import static java.lang.Math.max;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;
        // dp[i]= 2*i 크기의 직사각형을 채우는 방법의 수
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int [] p_sum = new int[n+1];
        for (int i =1; i<=n; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (i == 1) {
                p_sum[i] = num;
                continue;
            }
            p_sum[i] = p_sum[i-1] + num;
        }
        for (int i =0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            System.out.println(p_sum[b] - p_sum[a-1]);
        }
        


    }
}