
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {
	static int[] graph = new int[200004];
	static int k;
	static int[] cnt = new int[200001]; // 방법의 수도 카운트 해야함
	static void bfs(int idx) {
		Deque<Integer> que = new ArrayDeque<>();
		graph[idx] = 1;
		cnt[idx] = -1; 
		que.offerLast(idx);
		while(!que.isEmpty()) {
			int cur = que.pollFirst();
			if (cur == k) return; // 처음 도달하면 최단
			int[] nexts = {cur +1, cur-1, cur*2};
			for (int next : nexts) {
				if (next < 0 || next >=200000) continue;
				if (graph[next] != -1) continue;

				graph[next] = graph[cur] +1;
				cnt[next] = cur;
				que.offerLast(next);					

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
		 System.out.println(graph[k]-1);
		 ArrayList<Integer> list = new ArrayList<>();
		 for (int i=k; i !=-1; i = cnt[i]) {
			 list.add(i);
		 }
		 Collections.reverse(list);
		 for (int i : list) System.out.print(i+" ");
		 
	}
}