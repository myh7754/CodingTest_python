#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> v, visited;
int gy, gx,ret,count;
const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};
void dfs(int y, int x) {
    for (int i=0; i<4; i++) {
        int ny = dy[i] +y;
        int nx = dx[i] + x;
        if(0<=ny && ny<gy && 0<=nx && nx<gx) {
            if (visited[ny][nx]== 1) continue;
            if (v[ny][nx] == 0) {
                visited[ny][nx] =1;
                dfs(ny,nx);   
            }
        }
    }
}

int countCheese() {
    int cnt = 0;
    for (int y=0; y<gy; y++)
        for (int x=0; x<gx; x++)
            if (v[y][x] == 1) cnt++;
    return cnt;
}


int main() {
    cin >> gy >> gx;
    v.assign(gy, vector<int>(gx));
    for (int i=0; i<gy; i++) {
        for (int j =0; j<gx; j++) {
            cin >> v[i][j];
        }
    }
    
    int time = 0;
    int last = 0;
    while (true) {
        if (countCheese() ==0) {
            break;
        }
        visited.assign(gy, vector<int>(gx, 0));
        visited[0][0] = 1;
        dfs(0, 0);
        vector<pair<int,int>> melt;
        for (int y=0; y<gy; y++) {
            for (int x =0; x<gx; x++) {
                if (v[y][x] !=1) continue; // 치즈 부분만 고르기
                for(int dir=0; dir<4; dir++) {
                    int ny = y + dy[dir];
                    int nx = x + dx[dir];
                    if (ny<0||ny>=gy||nx<0||nx>=gx) continue;
                    // 치즈 중에 공기와 겉에 공기에 맡닿아 있는 부분만 고르기
                    // 반드시 외부 공기 0과 닿아있는 부분만 추가 되므로 내부의 0은 신경쓸 필요 없음
                    if (visited[ny][nx] == 1) {
                        melt.push_back({y,x});
                        break;
                    }
                }
            }
        }
        // 녹이기
        int count =0;
        for (auto [y,x] : melt) {
            v[y][x] = 0;
            count++;
        }
        time++;
        last = count; 
    }

    cout << time << "\n" << last << "\n";
}