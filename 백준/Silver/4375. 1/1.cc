#include <bits/stdc++.h>
using namespace std;                                  


int main() {
    int n;
    while (cin >> n) {
        long long num = 1; // 1, 11, 111... 이 될 변수
        int count = 1;     // 자리수 기록
        while (true) {
            if (num %n == 0) {
                cout << count << "\n";
                break;
            } 
            num = (num*10+1)%n;
            count ++;
        }
    }
    return 0;
}