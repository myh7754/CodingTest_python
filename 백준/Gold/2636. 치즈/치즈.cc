#include <bits/stdc++.h>
using namespace std;
int gy,gx;
vector<vector<int>> v,visited;

int dy[] = {0,0,-1,1};
int dx[] = {-1,1,0,0};

void dfs(int y, int x) {
    for (int i =0; i<4; i++) {
        int nx = dx[i] +x;
        int ny = dy[i] +y;
        if (0<=ny && ny <gy && 0<=nx && nx < gx) {
            if (visited[ny][nx] == 1 || v[ny][nx] == 1) continue;
            visited[ny][nx] =1;
            dfs(ny,nx);
        }
    }
}

int cntCz() {
    int cnt =0;
    for (int i=0; i<gy; i++) {
        for (int j=0; j<gx; j++) {
            if (v[i][j] == 1) {
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
        for (int j=0; j<gx; j++) {
            cin >> v[i][j];
        }
    }
    // 외부 공기를 전부 방문처리, 날짜 카운트 시작 O
    // 외부 공기와 닿아 있는 치즈 부분을 저장하고 O
    // 해당 저장을 0으로 변경 O
    // 만약 남은 그래프의 치즈가 0이라면 마지막 저장한 치즈 부분의 사이즈가 정답
    int day ;
    int cnt;
    while(true) {
        if (!cntCz()) {
            break;
        }
        visited.assign(gy,vector<int>(gx));
        dfs(0,0);
        day++;
        vector<pair<int,int>> cz;
        for (int y =0; y<gy; y++ ) {
            for (int x=0; x<gx; x++) {
                for (int i =0; i<4; i++) {
                    int nx = dx[i] +x;
                    int ny = dy[i] +y;
                    if (0<=ny && ny <gy && 0<=nx && nx < gx) {
                        if(visited[ny][nx]==1 && v[y][x] == 1) {
                            cz.push_back({y,x});
                            break;
                        }
                    }
                }                
            }
        }
        cnt = cz.size();
        for (auto it : cz) {
            v[it.first][it.second] = 0;
        }
    }

    cout << day << "\n" << cnt;
    return 0;
}