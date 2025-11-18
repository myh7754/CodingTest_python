import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());

        int T = Integer.parseInt(br.readLine());
        Deque<Integer> objects = new ArrayDeque<>();
        for (int i = 1; i <= T; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0 && !objects.isEmpty()) {
                objects.pollLast();
            } else {
                objects.add(num);
            }
        }
        int sum = objects.stream()
                .mapToInt(Integer::intValue)
                .sum();
        System.out.println(sum);

    }
}