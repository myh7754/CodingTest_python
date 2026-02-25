import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	static ArrayList<Character> opr;
	static ArrayList<Integer> nums;
	static int ans = Integer.MIN_VALUE;
	static int cal(char c, int a, int b) {
		if(c == '*') return a*b;
		if(c == '+') return a+b;
		if(c == '-') return a-b;
		return 0;
	}
	
	static void dfs(int idx, int cur) {
		if (idx == opr.size()) {
			ans = Math.max(ans, cur);
			return ;
		}
		// 괄호 없이 계산
		int v1 = cal(opr.get(idx), cur, nums.get(idx+1));
		dfs(idx+1, v1);
		
		// 괄호와 함께 계산
		if (idx+1 < opr.size()) {
			int inParen = cal(opr.get(idx+1), nums.get(idx +1), nums.get(idx +2));
			int v2 = cal(opr.get(idx), cur, inParen);
			dfs(idx +2, v2);
		}
		
	}
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String s = br.readLine();
		nums = new ArrayList<>();
		opr = new ArrayList<>();
		for (int i =0; i<s.length(); i++) {
			if(i%2 == 0)  nums.add(s.charAt(i)-'0');
			else opr.add(s.charAt(i));
		}
		
		dfs(0, nums.get(0));
		System.out.println(ans);
	}

}