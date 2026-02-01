#include <bits/stdc++.h>
using namespace std;
int a[26];
string word;
int main() {
    // 단어입력받기
    // 해당 단어에서 각 단어가 몇개 포함되어있는지 체크
    cin >> word;
    for (char b : word) {
        b -= 97;
        a[b] +=1;
    }

    for (int val: a) {
        cout << val << " ";
    }
    return 0;
}