#include <bits/stdc++.h>
using namespace std;
int gy,gx;
vector<vector<int>> v;
vector<int> visited;
int dfs(int here) {
    int cnt =1;
    visited[here] = 1;
    for (auto it: v[here]) {
        if (visited[it] == 1) continue;
        cnt += dfs(it);
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(0); 
	cin.tie(0);
    cin >> gy >> gx;
    v.assign(gy+1,vector<int>());
    v[0].push_back(0);
    for (int i = 1; i<=gx; i++) {
        int a,b;
        cin >> a >> b;
        v[b].push_back(a);
    }
    int mx = 0;
    vector<int> ret(gy+1, 0);
    for (int i=1; i<=gy; i++) {
        visited.assign(gy+1,0);
        ret[i] = dfs(i);
        mx = max(mx, ret[i]);
    }
    for (int i =1; i<=gy; i++) {
        if (ret[i] == mx) cout << i << " ";
    }
    return 0;
}