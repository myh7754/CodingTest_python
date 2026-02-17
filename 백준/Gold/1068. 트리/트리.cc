#include<bits/stdc++.h>
using namespace std;
vector<vector<int>> v;
int cnt;
int ez;
int dfs(int here) {
    if (here == ez) return 0; // 삭제된 노드는 없음

    int aliveChild = 0;
    int sum = 0;

    for (int it : v[here]) {
        if (it == ez) continue; // 삭제될 자식은 없는 취급
        aliveChild++;
        sum += dfs(it);
    }

    // 삭제되고 남은 자식이 0명이면 리프
    if (aliveChild == 0) return 1;
    return sum;
} 

int main() {
    int n;
    cin >> n;
    int num, root;
    v.assign(n,vector<int>());
    for (int i=0; i<n; i++) {
        cin >> num;
        if (num == -1) root = i;
        else v[num].push_back(i);
    }

    cin >> ez;
if (root == ez) {
        cout << 0 << "\n";
        return 0;
    }
    cout << dfs(root);

}