#include <bits/stdc++.h>
using namespace std;
int n,c;

bool isDigit(char c) {
    int test = c - '0';
    if (0<= test && test <10) {
        return true;
    } else {
        return false;
    }
}

bool cmp(string a, string b) {
    if(a.size() == b.size()) return a < b;
    return a.size() <  b.size();
}

int main() {
    // n줄을 입력받음

    // 숫자를 모두 찾고 숫자를 비내림차순으로 정리
    // 0는 생략
    // 글자를 보다 숫자가 나오면 가장 큰 숫자를 찾아야한다. -> 죽 10 200 300 400단위 숫자가능
    vector<string> ret;
    cin >> n;
    for (int i =0; i<n; i++) {
        string s;
        cin >> s;
        string num;
        bool prev = false;
        for (char ch: s) {
            if (isDigit(ch)) { // 숫자라면
                num += ch;
            } else { // 문자라면
                if (!num.empty()) {
                    // 맨 앞 0 제거
                    while (!num.empty() && num.front() == '0') {
                        num.erase(num.begin());
                    }
                    // 0만 있었다면
                    if (num.empty()) {
                        num = "0";
                    }
                    // 처리 다 끝났으면 결과값 넣고 초기화
                    ret.push_back(num);
                    num = "";
                }
            }
        }
        if (num.size()) {
            while (!num.empty() && num.front() == '0') {
                        num.erase(num.begin());
                    }
                    if (num.empty()) num = "0";
                    ret.push_back(num);
        }

    }

    sort(ret.begin(), ret.end(), cmp);
    for(string i : ret) cout << i << "\n";
    return 0;
}