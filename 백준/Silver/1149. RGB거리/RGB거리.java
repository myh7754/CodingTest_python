import java.io.*;
import java.util.*;

import static java.lang.Math.max;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ;

        int n = Integer.parseInt(br.readLine());
        int [][]arr = new int[n+1][3];
        // 1번집은 2번집과 색이 같지 않아야함
        // N번집은 N-1번집과 색이 같지 않아야함.
        // i(2<=i<=N-1)번 집은 i-1, i+1과 색이 같지 않아야함.
        for (int i =1; i<=n; i++) {
            // i번째 집
            // r g b를 입력
            st= new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken()); // Red
            arr[i][1] = Integer.parseInt(st.nextToken()); // Green
            arr[i][2] = Integer.parseInt(st.nextToken()); // Blue
        }
        int [][] dp = new int[n+1][3]; // i번째를 C로 칠했을 때 1..i까지의 최소비용
        // 초기값: 0번 집을 각각의 색으로 칠하는 비용
        dp[1][0] = arr[1][0];
        dp[1][1] = arr[1][1];
        dp[1][2] = arr[1][2];
        // 각 n번째 집이 n-1번집과 색이 같지 않은 경우
        for (int i=2; i<=n; i++) {
            dp[i][0] = Math.min(dp[i-1][1], dp[i-1][2]) + arr[i][0];
            dp[i][1] = Math.min(dp[i-1][0], dp[i-1][2]) + arr[i][1];
            dp[i][2] = Math.min(dp[i-1][0], dp[i-1][1]) + arr[i][2];
        }
        int answer = Math.min(dp[n][0], Math.min(dp[n][1], dp[n][2]));
        System.out.println(answer);
    }
}