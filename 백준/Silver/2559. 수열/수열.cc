#include <bits/stdc++.h>
using namespace std;

int n, k;

int main() {
    cin >> n >> k;
    vector<int> go(n);
    vector<int> p_sum(n);
    for (int i=0; i<n; i++) {
        cin >> go[i];
        if (i == 0) {
            p_sum[0] = go[i];
        } else {
            p_sum[i] = p_sum[i-1] + go[i];
        }
    }
    int m = p_sum[k-1];
    for (int i=k; i<n; i++) {
        m = max(m, p_sum[i] - p_sum[i-k]);
    }
    cout << m;

    return 0;
}