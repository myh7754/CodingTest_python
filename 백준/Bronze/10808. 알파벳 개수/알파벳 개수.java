import java.io.*; 
public class Main {
    public static void main(String[] args) throws Exception{
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter 선언
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // 첫번째 라인 값 3 입력
        String word = br.readLine();
        int[] count = new int[26];
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            count[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            System.out.print(count[i]+" ");
        }
    }
}