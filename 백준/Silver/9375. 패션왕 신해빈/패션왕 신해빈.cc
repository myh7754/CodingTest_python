#include <bits/stdc++.h>
using namespace std;

int n, m;

int main() {
    // 의상 조합 수 입력
    // 이 조합중 나올 수 있는 경우의 수 조합 - 아무것도 입지 않는 경우의수

    cin >> n;
    while(n--) {
        int num;
        cin >> num;
        map<string, int> v;
        for (int j = 0; j<num; j++) {
            string t, k;
            cin >> t >> k;
            v[k]++;
        }
        int i =1;
        for(auto it : v) {
            int count = it.second;
            i = i*(count+1);
        }
        cout << i-1 << "\n";   
    }

    
    return 0;
}