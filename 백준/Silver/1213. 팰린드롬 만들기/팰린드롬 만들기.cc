#include <bits/stdc++.h>
using namespace std;

int main() {
    string s; cin >> s; 
    map<char,int> count; 
    for (char it : s) { count[it]++; } 
    int isOdd = 0; 
    string ret = ""; 
    string left =""; 
    string oddStr = ""; 
    for (char i = 'Z'; i>='A'; i--) { 
        char word = i; 
        int it = count[i]; 
        if(it %2 == 1) { 
            isOdd++;
            oddStr = string(1,word);
            it -=1;
            if(isOdd >=2) { 
                break; 
            }
        }
        left += string(it/2,word);
    }
    string right = left;
    reverse(right.begin(),right.end());
    ret =  right + oddStr + left;
    if(isOdd >=2) { 
        cout << "I'm Sorry Hansoo" <<"\n"; 
    } else { 
        cout << ret << "\n"; 
    } 
    return 0;
}