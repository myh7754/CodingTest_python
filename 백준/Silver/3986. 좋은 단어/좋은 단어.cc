#include <bits/stdc++.h>
using namespace std;                                  


int main() {
    int test;
    cin >> test;
    string s;
    int cnt= 0;
    for (int i =0; i <test; i++) {
        cin >> s;
        vector<char> left;
        for(char word: s) {
             if (left.empty()) {
                 left.push_back(word);
                 continue;
             } 
            int endIdx = left.back();
            if (endIdx == word) {
                left.pop_back();
            } else {
                left.push_back(word);
            }
        }
        if(left.empty()) {
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}