
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	static Boolean ab(String prefix, String suffix, String target) {
		if (target.length() < prefix.length() + suffix.length()) return false;
		if (!target.startsWith(prefix)) return false;
        if (!target.endsWith(suffix)) return false;

        return true;
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String s = br.readLine();
		int idx = s.indexOf("*");
		String prefix = s.substring(0, idx);
		String suffix = s.substring(idx+1);
		for (int i=0; i<n; i++) {
			String tar = br.readLine();
			if(ab(prefix, suffix, tar)) {
				System.out.println("DA");
			} else {
				System.out.println("NE");
			}
			
		}
		
	}

}
