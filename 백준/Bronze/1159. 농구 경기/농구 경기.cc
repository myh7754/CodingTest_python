#include <bits/stdc++.h>
using namespace std;
int a[26];
int test;
string word;
string temp;
int main() {
    // 카운트 입력
    // 이름 수 입력
    // map에 해당 이름이 있다면 +1
    // map을 돌며 해당 카운트가 5 이상인게 있다면
    // a단어 배열에 +1
    // 단어 배열에 따라 결과
    cin >> test;
    for (int i =0; i<test; i++) {
        cin >> word;
        a[word[0]-'a']++;
    }
    string j;
    for (int i = 0; i<26; i++) {
        if (a[i] >=5) {
            j+=i+'a';
        }
    }

    if (j.size()) {
        cout << j; 
    } else {
        cout <<"PREDAJA";
    }
    return 0;
}