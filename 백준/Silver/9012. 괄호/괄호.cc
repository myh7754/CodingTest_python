#include <bits/stdc++.h>
using namespace std;

int main() {
    int test;
    cin >> test;
    while(test--) {
        string n;
        cin >> n;
        vector<char> left;
        for (char ch : n ) {
            if (ch == '(') {
                left.push_back('(');
            }else if (ch ==')' && !left.empty()) {
                left.pop_back();
            } else {
                left.push_back('b');
                break;
            }
        }
        if (!left.empty()) {
            cout << "NO" << "\n";
        } else {
            cout << "YES" << "\n";
        }        
    }

    return 0;
}