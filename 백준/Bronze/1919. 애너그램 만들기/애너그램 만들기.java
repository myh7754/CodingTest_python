import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());

        String a = br.readLine();
        String b = br.readLine();
        int[] word1 = new int[26];
        int[] word2 = new int[26];
        for (char c : a.toCharArray()) {
            word1[c - 'a']++;
        }
        for (char c : b.toCharArray()) {
            word2[c - 'a']++;
        }
        int result = 0;
        for (int i = 0; i < 26; i++) {
            if (word1[i] != word2[i]) {
                result += Math.abs(word1[i] - word2[i]);
            }
        }

        System.out.println(result);

    }
}