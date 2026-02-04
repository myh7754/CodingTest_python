#include <bits/stdc++.h>
using namespace std;
int n,m,num,j;

int main() {
    cin>>n>>m;
    cin >> num ;
    int left = 1;
    int count =0;
    for (int i=0; i<num; i++) {
        cin >> j;
        int right = left + m-1;

        if(left<= j && j<=right) continue;
        else {
            if(j < left) {
                count += (left - j);
                left -= (left-j);
            } else {
                count += (j - right);
                left += (j-right);
            }
        }
        
    }

    cout << count;
    return 0;
}