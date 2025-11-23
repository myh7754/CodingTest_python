import java.io.*;
import java.util.*;

public class Main {
    static int gy,gx;
    static int[][] graph;
    static int end_x;
    static int end_y;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            gy = Integer.parseInt(st.nextToken());
            gx = gy;
            st = new StringTokenizer(br.readLine());
            int start_x = Integer.parseInt(st.nextToken());
            int start_y = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            end_x = Integer.parseInt(st.nextToken());
            end_y = Integer.parseInt(st.nextToken());
            Deque<int[]> myque = new ArrayDeque<>();
            myque.add(new int[]{start_x,start_y});
            graph = new int[gy][gy];
            for(int i=0;i<gy;i++) {
                Arrays.fill(graph[i],0);
            }

            graph[start_x][start_y] = 1;
            
            bfs(myque);
        }

    }

    public static void bfs(Deque<int[]> myque) {
        int[] dy = {2,1,-1,-2,-2,-1,1,2};
        int[] dx = {1,2,2,1,-1,-2,-2,-1};
        while (!myque.isEmpty()){
            int[] cur = myque.poll();
            int x = cur[0];
            int y = cur[1];
            if (x == end_x &&  y == end_y){
                System.out.println(graph[x][y]-1);
                break;
            }
            for(int i = 0;i<8;i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                if (0<=ny&& ny <gy && 0<=nx && nx<gy ){
                    if (graph[nx][ny]==0){
                        graph[nx][ny]= graph[x][y]+1;
                        myque.add(new int[]{nx,ny});
                    }
                }
            }
        }
    }
}