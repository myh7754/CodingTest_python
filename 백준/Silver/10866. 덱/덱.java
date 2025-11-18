import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> left = new ArrayDeque<>();

        for (int i = 1; i <= T; i++) {
            String[] input = br.readLine().split(" ");
            String cmd = input[0];
            int idx = (input.length > 1) ? Integer.parseInt(input[1]) : 0;
            if(cmd.equals("push_front")){
                left.addFirst(idx);
            } else if (cmd.equals("push_back")){
                left.add(idx);
            } else if (cmd.equals("pop_front")){
                if(left.isEmpty()){
                    System.out.println(-1);
                } else {
                    System.out.println(left.pollFirst());
                }
            }  else if (cmd.equals("pop_back")){
                if(left.isEmpty()){
                    System.out.println(-1);
                } else {
                    System.out.println(left.pollLast());
                }
            } else if(cmd.equals("size")){
                System.out.println(left.size());
            } else if(cmd.equals("empty")){
                if(left.isEmpty()){
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            } else if(cmd.equals("front")){
                if(left.isEmpty()){
                    System.out.println(-1);
                } else {
                    System.out.println(left.peekFirst());
                }
            } else if(cmd.equals("back")){
                if(left.isEmpty()){
                    System.out.println(-1);
                } else {
                    System.out.println(left.peekLast());
                }
            }
        }


    }
}