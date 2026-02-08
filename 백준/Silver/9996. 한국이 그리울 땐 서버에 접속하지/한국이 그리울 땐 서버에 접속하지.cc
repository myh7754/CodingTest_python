#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    string s;
    string left;
    string right;
    cin >> s;
    int idx = s.find("*");
    left = s.substr(0,idx);
    right = s.substr(idx+1,s.size());
    
    while(t--) {
        string word;
        cin >> word;
        if(word.size() < left.size() + right.size()) {
            cout << "NE\n";
        }else {if(left == word.substr(0, left.size()) && right == word.substr(word.size()-right.size(), right.size())) {
            cout << "DA" << "\n";
        } else {
            cout << "NE" << "\n";
        }
              }

    }
    
    return 0;
}