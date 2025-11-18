import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            Deque<Character> left = new ArrayDeque<>();
            Deque<Character> right = new ArrayDeque<>();
            String word = br.readLine();

            for (char cmd : word.toCharArray()) {
                if (cmd == '<') {
                    if(!left.isEmpty()){
                        right.push(left.pop());
                    }
                } else if(cmd == '>') {
                    if(!right.isEmpty()){
                        left.push(right.pop());
                    }
                } else if(cmd == '-') {
                    if(!left.isEmpty()){
                        left.pop();
                    }
                } else {
                    left.push(cmd);
                }

            }
            StringBuilder sb = new StringBuilder();
            while(!left.isEmpty()){
                sb.append(left.pollLast());
            }
            while(!right.isEmpty()){
                sb.append(right.poll());
            }
            System.out.println(sb);
        }
    }
}