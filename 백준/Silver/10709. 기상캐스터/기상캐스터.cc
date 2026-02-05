#include <bits/stdc++.h>
using namespace std;
int gy, gx,y,x;
int dx[] = {1};
int dy[] = {0};
int main() {
    // y = H  x = W
    cin >> gy >> gx;
    vector<vector<char>> graph(gy, vector<char>(gx));
    vector<vector<int>> visited(gy,vector<int>(gx,-1));
    for (int i=0; i<gy; i++) {
        string s;
        cin >> s;
        for (int j =0; j<gx; j++) {
            graph[i][j] = s[j];
        }
    }
    deque<pair<int,int>> start;
    for (int i=0; i<gy; i++) {
        for (int j =0; j<gx; j++) {
            if (graph[i][j] == 'c') {
                start.push_back({i,j});
                visited[i][j] = 0;
            }
        }
    }

    while(start.size()) {
        tie(y,x) = start.front(); start.pop_front();

        int nx = x + dx[0];
        int ny = y + dy[0];

        if(ny< 0 || ny>=gy || nx<0|| nx>=gx) continue;
        if(graph[ny][nx] == 'c' || visited[ny][nx] != -1) {
            continue;
        }
        visited[ny][nx] = visited[y][x] +1;
        start.push_back({ny,nx});

    }

    for (int i = 0; i <gy; i++) {
        for (int j=0; j<gx; j++) {
            cout << visited[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}