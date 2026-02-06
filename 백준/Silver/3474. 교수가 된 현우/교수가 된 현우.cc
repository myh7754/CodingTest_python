#include <bits/stdc++.h>
using namespace std;
int n,a;
int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    while(n--) {
        cin >>a;
        int ret = 0;
        for (int i =5; i<=a; i*=5) {
            ret += a/i;
        }
        cout << ret <<"\n";
    }
    return 0;
}