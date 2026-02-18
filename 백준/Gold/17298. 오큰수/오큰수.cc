#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int num;
    cin >> num;

    vector<int> v(num);
    for (int i = 0; i < num; i++) {
        cin >> v[i];   // ✅ a[i] → v[i]
    }

    vector<int> ret(num, -1);  // 기본값 -1
    vector<int> st;            // 인덱스를 저장할 스택 역할

    for (int i = 0; i < num; i++) {

        // 현재 값이 스택 top 값보다 크면 오큰수 확정
        while (!st.empty() && v[st.back()] < v[i]) {
            ret[st.back()] = v[i];
            st.pop_back();
        }

        // 아직 오큰수 모르는 인덱스는 스택에 저장
        st.push_back(i);
    }

    for (int i = 0; i < num; i++) {
        cout << ret[i] << (i + 1 == num ? '\n' : ' ');
    }

    return 0;
}
