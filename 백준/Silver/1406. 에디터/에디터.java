import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());

        String word = br.readLine();
        int T = Integer.parseInt(br.readLine());
        Deque<Character> left = new ArrayDeque<>();
        Deque<Character> right = new ArrayDeque<>();
        for (char c : word.toCharArray()) {
              left.push(c);
        }
        for (int i = 0; i < T; i++) {

            String[] input = br.readLine().split(" ");
            String command = input[0];
            if(command.equals("L")){
                if (!left.isEmpty()) {
                    right.push(left.pop());
                }
            } else if (command.equals("D")) {
                if (!right.isEmpty()) {
                    left.push(right.pop());
                }
            } else if (command.equals("B")) {
                if (!left.isEmpty()) {
                    left.pop();
                }
            } else if (command.equals("P")) {
                left.push(input[1].charAt(0));
            }

        }
        StringBuilder sb = new StringBuilder();
        while (!left.isEmpty()) { 
            sb.append(left.pollLast());
        }
        while (!right.isEmpty()) {
            sb.append(right.poll());
        }
        System.out.println(sb);

    }
}