import java.io.*;
import java.util.*;

public class Main {
	static int n = 9;
	static int k = 7;
	static int[] selected,arr;
	
	static void comb(int idx, int dept) {
		if(dept == k) {
			int sum =0;
			for (int j=0; j<k; j++) {
				sum += selected[j];
			}
			if (sum ==100) {
				Arrays.sort(selected);
				StringBuilder sb = new StringBuilder();
				for (int x : selected) sb.append(x).append("\n");
				System.out.println(sb.toString());
                System.exit(0);
			}
			
			return ;
		}
		
		for (int i=idx; i<n; i++) {
			selected[dept] = arr[i];
			comb(i +1, dept+1);
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		arr = new int[n];
		selected = new int[k];
		for (int i =0; i<n; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		
		comb(0,0);
		
		
	}
	
}
