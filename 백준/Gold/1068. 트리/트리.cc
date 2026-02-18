#include <bits/stdc++.h>
using namespace std;
int num, r, root;
vector<vector<int>> v;
int dfs(int here) {
    int cnt=0, child = 0;
    for (int it : v[here]) {
        if (it == r) continue;
        cnt += dfs(it);
        child++;
    }
    if (child == 0) return 1;
    return cnt;
}

int main() {
    cin >> num;
    v.assign(num,vector<int>());
    for (int i=0; i<num; i++) {
        int k =0;
        cin >> k;
        if (k == -1) root = i;
        else v[k].push_back(i);
    }
    cin >> r;
    if (r== root) {
        cout << 0 ; 
        return 0;
    }
    cout << dfs(root);
   
    return 0;
}