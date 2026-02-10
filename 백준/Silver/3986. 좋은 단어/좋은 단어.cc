#include <bits/stdc++.h>
using namespace std;

int main() {
    // 같은 단어가 홀수일 경우
     string s;
    int n;
    cin >> n;
    int count =0;
    for (int i =0; i<n; i++) {
        cin >> s;
        vector<char> v;
        for (char word: s) {
            if (v.size()) {
                if (v.back() == word) {
                    v.pop_back();
                } else {
                    v.push_back(word);
                }
            } else {
                v.push_back(word);
            }
        }
        
        if (!v.size()) {
            count++;
        }
    }
    cout << count;
    return 0;
}