import java.io.*;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    static int gy,gx;
    static char[][] graph;
    static int[][] fire_graph;
    static int[][] jihun_graph;
    static int end_x;
    static int end_y;
    static int A,B,C;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        A = Integer.parseInt(st.nextToken());
        B = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        
        System.out.println(power(A,B));

    }

    static long power(int a, int b) {
        if (b == 0)
            return 1;
        long half = power(a, b / 2);
        long result = (half*half)%C;
        if (b % 2 == 1) {
            result= (result *a)%C ;
        }
        return result;

    }
}