import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static int[] graph = new int[200004];
	static int k;
	static long[] cnt = new long[200001]; // 방법의 수도 카운트 해야함
	static void bfs(int idx) {
		Deque<Integer> que = new ArrayDeque<>();
		graph[idx] = 1;
        cnt[idx] = 1;
		que.offerLast(idx);
		while(!que.isEmpty()) {
			int cur = que.pollFirst();
			int[] nexts = {cur +1, cur-1, cur*2};
			for (int next : nexts) {
				if (next < 0 || next >=200000) continue;
				if (graph[next] == -1) { // 처음 방문이라면
					graph[next] = graph[cur] +1;
					cnt[next] = cnt[cur];
					que.offerLast(next);					
				} else if (graph[next] == graph[cur]+1) { // 이미 방문했을 때 같은 최단거리로 또 도달했다면
					cnt[next] += cnt[cur];
					
				}

			}
		}
	}
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		 st = new StringTokenizer(br.readLine());
		 int n = Integer.parseInt(st.nextToken());
		 k = Integer.parseInt(st.nextToken());
		 Arrays.fill(graph, -1);
		 bfs(n);
		 System.out.println(graph[k] -1 );
		 System.out.println(cnt[k]);       // 방법 수 출력
	}

}
