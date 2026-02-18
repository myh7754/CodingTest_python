#include <bits/stdc++.h>
using namespace std;
int gy,gx,ret,cnt;
vector<vector<int>> v,visited,grid;
vector<pair<int,int>> wallList,start;
int dy[] = {0,0,-1,1};
int dx[] = {-1,1,0,0};

void dfs(int y, int x) {
    for (int i =0; i<4; i++) {
        int nx = dx[i] +x;
        int ny = dy[i] +y;
        if (0<=ny && ny <gy && 0<=nx && nx < gx) {
            if (visited[ny][nx] == 1 || v[ny][nx] == 1) continue;
            visited[ny][nx] =1;
            grid[ny][nx] = 2;
            dfs(ny,nx);
        }
    }
}

int solve() {
    visited.assign(gy,vector<int>(gx));
    for (auto it : start) {
        dfs(it.first, it.second);    
    }
    int cnt =0;
    for (int i=0; i<gy; i++) {
        for (int j=0; j<gx; j++) {
            if(grid[i][j] == 0) {
                cnt++;
            }
        }
    }
    return cnt;
}

int main() {
    cin >> gy >>gx;
    v.assign(gy,vector<int>(gx));    
    for (int i=0; i<gy; i++) {
        for(int j=0; j<gx; j++) {
            cin >> v[i][j];
            if (v[i][j] == 2) start.push_back({i,j});
            if (v[i][j] == 0)  wallList.push_back({i,j});
        }
    }

    // 1. 벽을 세운다 O
    // 2. dfs한다
    // 3. 안전구역을 확인한다. o
    // 4. 원복한다. o 
    int mx = 0;
    for (int i =0; i<wallList.size(); i++) {
        for (int j=i+1; j<wallList.size(); j++) {
            for(int k=j+1; k<wallList.size(); k++) {
                v[wallList[i].first][wallList[i].second] = 1;
                v[wallList[j].first][wallList[j].second] = 1;
                v[wallList[k].first][wallList[k].second] = 1;
                grid = v;
                mx = max(mx, solve());
                v[wallList[i].first][wallList[i].second] = 0;
                v[wallList[j].first][wallList[j].second] = 0;
                v[wallList[k].first][wallList[k].second] = 0;
            }
        }
    }

    cout << mx;
    return 0;
}