import java.io.*;
import java.util.*;

public class Main {
    static int gy,gx;
    static char[][] graph;
    static int[][] fireTime;
    static boolean[][] visited;
    static int[][] jgraph;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        gy = Integer.parseInt(st.nextToken());
        gx = Integer.parseInt(st.nextToken());
        graph = new char[gy][gx];
        visited = new boolean[gy][gx];
        fireTime = new int[gy][gx];
        jgraph = new int[gy][gx];
        Deque<int[]> fireQue = new ArrayDeque<>();
        Deque<int[]> jihunQue = new ArrayDeque<>();

        for (int y = 0; y <gy; y++) {
            Arrays.fill(fireTime[y], -1);
            Arrays.fill(jgraph[y], -1);
        }

        for (int y = 0; y< gy; y++) {
            String line = br.readLine();
            for (int x = 0; x < gx; x++) {
                graph[y][x] = line.charAt(x);

                if (graph[y][x] == 'F') {
                    fireQue.add(new int[]{y, x});
                    fireTime[y][x] = 0;
                }

                if (graph[y][x] == 'J') {
                    jihunQue.add(new int[]{y, x});
                    jgraph[y][x] = 0;
                }
            }
        }

        int[] dy = {1,-1,0,0};
        int[] dx = {0,0,1,-1};
        while (!fireQue.isEmpty()) {
            int[] cur =  fireQue.poll();
            int y = cur[0];
            int x = cur[1];
            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0<=nx && nx<gx && 0<=ny && ny<gy) {
                    if (graph[ny][nx] == '.'&& fireTime[ny][nx] == -1) {
                        fireTime[ny][nx] = fireTime[y][x] + 1;
                        fireQue.add(new int[]{ny, nx});
                    }
                }
            }
        }

        while (!jihunQue.isEmpty()) {
            int[] cur = jihunQue.poll();
            int y = cur[0];
            int x = cur[1];
            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (0<=nx && nx<gx && 0<=ny && ny<gy) {
                    if (graph[ny][nx] == '.' && jgraph[ny][nx] == -1) {
                        if (fireTime[ny][nx] == -1 || fireTime[ny][nx] > jgraph[y][x] + 1) {
                            jgraph[ny][nx] = jgraph[y][x] + 1;
                            jihunQue.add(new int[]{ny, nx});
                        }
                    }
                } else {
                    System.out.println(jgraph[y][x]+1);
                    System.exit(0);
                }
            }
        }

        System.out.println("IMPOSSIBLE");

    }


}