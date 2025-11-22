import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // BufferedReader 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st ; // = new StringTokenizer(br.readLine());
        String[] split = br.readLine().split(" ");
        int gy = Integer.parseInt(split[0]);
        int gx = Integer.parseInt(split[1]);
        int[][] graph = new int[gy][gx];

        for (int i =0; i <gy; i++) {
            String st = br.readLine();
            for (int j =0; j < gx; j++) {
                graph[i][j] = st.charAt(j) - '0';
            }
        }
        Deque<Integer> result = new ArrayDeque<>();
        Deque<int[]> myque = new ArrayDeque<>();
//        for (int i = 0; i < gy; i++) {
//            for (int j = 0; j < gx; j++) {
//                if (graph[i][j] == 1) {
//                    int bfs = bfs(graph, i, j, gy, gx, myque);
//                    result.add(bfs);
//                }
//            }
//        }
        bfs(graph, 0,0,gy,gx,myque);
        System.out.println(graph[gy-1][gx-1]);

    }
    public static int bfs(int[][] graph,int y, int x,int gy, int gx,Deque<int[]> myque ) {
        myque.add(new int[]{y,x});
        graph[y][x] = 1;
        int count = 1;
        while (!myque.isEmpty()) {
            int[] cur = myque.poll();
            y = cur[0];
            x = cur[1];
            int [] dy = {0,0,1,-1};
            int [] dx = {1,-1,0,0};
            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0<=ny && ny<gy && 0<= nx && nx<gx ) {
                    if (graph[ny][nx] == 1) {
                        graph[ny][nx] = graph[y][x] +1;
                        myque.add(new int[]{ny,nx});
                        count +=1;
                    }

                }
            }
        }
        return count;
    }
}