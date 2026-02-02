#include <bits/stdc++.h>
using namespace std;

int main() {
    int n , m;
    
    cin >> n;
    cin >> m;
    int cnt[n];
    for (int i = 0; i<n; i++) {
        cin >> cnt[i];
    }

    
    // 재료는 번호를 갖고 있다.
    // 두 재료의 번호를 합쳐 M이 되면 갑옷 생성
    // 총 몇개의 갑옷이 생성 가능한가
    int result = 0;
    // 총 n개중에 2개를 뽑아서 m이 되는 경우의 수를 찾아라
    // 순서가 상관 있으므로 조합 써야함
    for (int i =0; i<n; i++) {
        for (int j=i+1; j<n; j++) {
            if (cnt[i] + cnt[j] == m) {
                result++;
            }
        }
    }
    cout << result;
    return 0;
}