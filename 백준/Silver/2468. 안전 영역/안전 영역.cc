#include <bits/stdc++.h>
using namespace std;
int max_size = 51;
int gy, gx, y,x;
int ny[4] = {0,0,-1,1};
int nx[4] = {-1,1,0,0};
vector<vector<int>> graph;
vector<vector<int>> visited;

int dfs(int y,int x,int d) {
    visited[y][x] = 1;
    for (int i =0; i<4; i++) {
        int dx = x+nx[i];
        int dy = y+ny[i];
        if(dx<0||dx>=gx||dy<0||gy<=dy) continue;
        if(visited[dy][dx] || graph[dy][dx] <=d) continue;
        dfs(dy,dx, d);
    }
    return 1;
}


int main() {
    cin >> gy;
    gx = gy;
    graph.assign(gy,vector<int>(gx,0));
    for (int i =0; i < gy; i++) {
        for(int j =0; j<gx; j++) {
            cin >> graph[i][j];
        }
    }
    int totalCount = 1;
    for(int n = 1; n<101; n++) {
        visited.assign(gy,vector<int>(gx,0));
        deque<pair<int,int>> q;
        deque<int> count;
        for (int i =0; i<gy; i++) {
            for (int j=0; j<gx; j++) {
                if (graph[i][j] >n && !visited[i][j]) {
                    count.push_front(dfs(i,j,n));
                }
            }
        }
        totalCount = max(totalCount, (int)count.size());
    }
    cout << totalCount;
    
    
    return 0;
}