import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int K = Integer.parseInt(input[1]);
        ArrayDeque<Integer> left = new ArrayDeque<>();
        for(int i=1;i<=N;i++){
            left.add(i);
        }
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        while(!left.isEmpty()){
            for(int i=0;i<K-1;i++){
                left.add(left.pollFirst());
            }
            sb.append(left.pollFirst());
            if (left.isEmpty()){
                sb.append(">");
                break;
            }
            sb.append(", ");
        }
        System.out.println(sb);

    }
}