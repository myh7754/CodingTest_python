import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    static int[][] paper;
    static boolean[][] visited;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        
        paper = new int[n][m];
        visited = new boolean[n][m];
        
        // 그림 정보 입력받기
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        int count = 0; // 그림 개수
        int maxArea = 0; // 가장 넓은 그림의 넓이
        
        // 모든 칸을 탐색
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // 색칠되어 있고 아직 방문하지 않은 곳에서 BFS 시작
                if (paper[i][j] == 1 && !visited[i][j]) {
                    int area = bfs(i, j);
                    count++;
                    maxArea = Math.max(maxArea, area);
                }
            }
        }
        
        System.out.println(count);
        System.out.println(maxArea);
    }
    
    static int bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{x, y});
        visited[x][y] = true;
        int area = 1; // 현재 그림의 넓이
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curX = current[0];
            int curY = current[1];
            
            // 상하좌우 탐색
            for (int i = 0; i < 4; i++) {
                int nx = curX + dx[i];
                int ny = curY + dy[i];
                
                // 범위 체크
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    // 색칠되어 있고 아직 방문하지 않은 곳
                    if (paper[nx][ny] == 1 && !visited[nx][ny]) {
                        queue.offer(new int[]{nx, ny});
                        visited[nx][ny] = true;
                        area++;
                    }
                }
            }
        }
        
        return area;
    }
}