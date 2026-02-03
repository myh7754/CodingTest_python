#include <bits/stdc++.h>
using namespace std;
int max_size = 51;
int gy, gx, y,x;
int ny[4] = {0,0,-1,1};
int nx[4] = {-1,1,0,0};
vector<vector<int>> graph;
vector<vector<int>> visited;

int bfs(int y,int x) {
    int count =0;
    visited[y][x] = 1;
    deque<pair<int,int>> q;
    q.push_front({y,x});
    while(q.size()) {
        tie(y,x) = q.front();
        q.pop_front();
        for(int i =0; i<4; i++) {
            int dx = x + nx[i];
            int dy = y + ny[i];
            if(dx<0||dx>=gx||dy<0||dy>=gy) continue;
            if(visited[dy][dx] !=0 || graph[dy][dx] == 0) continue;
            q.push_front({dy,dx});
            visited[dy][dx] = visited[y][x]+1;
            count +=1;
        }
    }
    return count;
}

int main() {
    int test;
    cin >> test;
    for (int i =0; i< test; i++) {
        int pos;
        cin >> gy >> gx >> pos;
        graph.assign(gy, vector<int>(gx, 0));
        visited.assign(gy, vector<int>(gx, 0));
        for (int i =0; i<pos; i++) {
            cin >> y >> x;
            graph[y][x] = 1;
        }

        // 플루이드 개수를 찾기
        deque<int> count; 
        for (int i =0; i<gy; i++) {
            for (int j=0; j<gx; j++) {
                if(graph[i][j] == 1 && visited[i][j] ==0) {
                    count.push_front(bfs(i,j));
                }
            }
        }
        cout << count.size() << '\n';
    }
    return 0;
}