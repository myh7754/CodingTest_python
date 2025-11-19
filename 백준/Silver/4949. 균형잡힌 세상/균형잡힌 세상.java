import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());


        while (true) {
            String input = br.readLine();
            if (input.equals(".")) {
                break;
            }
            ArrayDeque<Character> dq = new ArrayDeque<>();
            boolean t = true;
            for (char word : input.toCharArray()) {
                if ( word == '(' || word == '[') {
                    dq.add(word);
                } else if ( word == ')') {
                    if (dq.isEmpty() || dq.peekLast() != '(') {
                        t = false;
                        System.out.println("no");
                        break;
                    } else if (dq.peekLast() == '(') {
                        dq.pollLast();
                    }
                } else if ( word == ']') {
                    if (dq.isEmpty() || dq.peekLast() != '[') {
                        System.out.println("no");
                        t = false;
                        break;
                    } else if (dq.peekLast() == '[') {
                        dq.pollLast();
                    }
                }
            }
            if (t && dq.isEmpty()) {
                System.out.println("yes");
            } else if (t && !dq.isEmpty()) {
                System.out.println("no");
            }
        }


    }
}