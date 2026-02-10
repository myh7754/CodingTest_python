#include <bits/stdc++.h>
using namespace std;

int n, m;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    // 도감 만들기
    cin >> n >> m;
    map<string, int> v;
    map<int, string> k;
    for (int i =0; i<n; i++) {
        string s;
        cin >> s;
        v[s] = i+1;
        k[i+1] = s;
    }
    
    // index 카운팅
    for (int i =0; i<m; i++) {
        string s;
        cin >> s;
        if(!isdigit(s[0])) {
            cout << v[s] <<"\n"; 
        } else {
            int idx = stoi(s);
            cout << k[idx] << "\n";
        }
    }
    return 0;
}