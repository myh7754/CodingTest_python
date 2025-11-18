import javax.swing.text.html.parser.Parser;
import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception{
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st ; // = new StringTokenizer(br.readLine());

        String a = br.readLine();

        int[] count = new int[10];

        for (char word : a.toCharArray()) {
            count[word-'0']++;
        }
        count[6]= (count[6] +count[9] + 1)/2 ; // 올림
        count[9] = 0;

        int m = count[6];
        for (int i = 0 ; i<10 ; i++){
            if(i == 6) {
                continue;
            }
            if(count[i] > m) {
                m = count[i];
            }
        }

        System.out.print(m);

    }
}