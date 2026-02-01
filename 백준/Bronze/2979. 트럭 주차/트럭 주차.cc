#include <bits/stdc++.h>
using namespace std;
int a, b, c;
int st, ed;
int parking[101];
string word;
int main() {
    // a, b, c원 입력받기 
    // 1대당 a원 ,2대 b원 . 3대는 c원

    cin >> a >> b >> c;
    for (int i =0; i<3; i++) {
        cin >> st >> ed;
        for (int j = st; j <ed; j++) {
            parking[j] +=1;
        }
    }
    int sum = 0;
    for (int val : parking) {
        if (val == 1) {
            sum +=val*a;
        } else if( val==2) {
            sum +=val*b;
        } else if(val ==3) {
            sum+=val*c;
        }
    }

    
    cout << sum;
    return 0;
}