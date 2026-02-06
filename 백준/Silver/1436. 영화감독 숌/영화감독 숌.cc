#include <bits/stdc++.h>
using namespace std;

int n;
int main() {
    cin >> n; 
    vector<int> v;
    int i = 666;
    for (;; i++) {
        string s = to_string(i);
        if(s.find("666") != string::npos) {
            v.push_back(i);
        }
        if ((int) v.size() == n) {
            break;
        }
    }
    cout << v[n-1];
    return 0;
}