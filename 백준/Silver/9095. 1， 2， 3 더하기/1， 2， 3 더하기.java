import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;
        st= new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        for (int b=0; b<T; b++) {
            int n = Integer.parseInt(br.readLine());
            int [] dp = new int[n+3]; // dp[i]는 i를 1,2,3으로 나타내는 방법의 수
            dp[1] = 1;
            dp[2] = 2;
            dp[3] = 4;
            if (n >3) {
                for (int i=4; i<=n; i++) {
                    dp[i] = dp[i-1]+dp[i-2]+dp[i-3];
                }
            }
            System.out.println(dp[n]);
        }
    }
}