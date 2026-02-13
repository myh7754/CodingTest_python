#include <bits/stdc++.h>
using namespace std;
vector<vector<int>> v;
vector<vector<int>> visited;
int gy,gx,k,x,y;
int dx[] = {0,0,1,-1};
int dy[] = {-1,1,0,0};
int dfs(int y, int x) {
    visited[y][x] =1;
    int ret = 1;
    for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0<=ny && ny<gy && 0<= nx && nx < gx) {
            if (visited[ny][nx] !=0 || v[ny][nx] == 1) continue;
            ret += dfs(ny,nx);
        }
    }
    return ret;
}

int main() {
    vector<int> ret;
    cin >> gy >> gx >> k;
    v.assign(gy, vector<int>(gx,0));
    visited.assign(gy, vector<int>(gx,0));
    for (int i=0; i<k; i++) {
        int gsy,gsx, gey,gex;
        cin >> gsx >> gsy >> gex >> gey;
        for (int j = gsy; j<gey; j++) {
            for (int t= gsx; t<gex; t++) {
                v[j][t] = 1;
            }
        }
    }
            int count= 0;
        for (int j = 0; j<gy; j++) {
            for(int t=0; t<gx; t++) {
                if(v[j][t] == 0 && visited[j][t] ==0) {
                    ret.push_back(dfs(j,t));
                }
            }
        }
    sort(ret.begin(), ret.end());
    cout << ret.size() << "\n";
    for(int a : ret) cout << a << " "; 
    
    return 0;
}