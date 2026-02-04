#include <bits/stdc++.h>
using namespace std;
int n,c;

bool isVowel(char ch) {
    return ch =='a' || ch == 'e' || ch =='o' || ch=='i'|| ch=='u';
}

bool valid(string word) {
    // 1. word에서 aeiou 중 없으면 fail
    if (word.find_first_of("aeiou") == string:: npos) return false;
    // 다른방법
    // bool hasVowel = false;
    // for (char ch : word) {
    //     if (ch =='a' || ch == 'e' || ch =='o' || ch=='i'|| ch=='u') {
    //         hasVowel = true;
    //         break;
    //     }
    // }
    // if (!hasVowel) {
    //     return hasVowel;
    // }
    
    // 2. 모음 ,자음이 3개 연속이면 fail
    char temp ='\0';
    int count = 0;
    bool prev = isVowel(word[0]);
    for(char ch: word) {
        if (isVowel(ch) == prev) {
            count++;
        } else {
            prev = isVowel(ch);
            count =1;
        }
        if (count == 3) {
            return false;
        }
    }

    
    // 3. 같은 글자가 2번 연속이면 fail ee랑 oo는 허용
    count = 0;
    temp = '\0';
    for(char ch: word) {
        if (ch == temp) {
            count++;
        } else {
            temp = ch;
            count = 1;
        }
        if (count == 2) {
            if (ch == 'e' || ch=='o') continue;
            else return false;
        }
    }

    return true;
}

int main() {
    // 아에이오우중 하나 포함
    // 모음 3개 자음3개 연속 x
    // 같은 글자가 두번오면 안되는데 ee oo는 허용
    string s;
    cin >> s;
    while (s != "end") {
        if (valid(s)) {
            cout << "<" << s << ">" << " is acceptable." << "\n" ;
        } else {
            cout << "<" << s << ">" << " is not acceptable." << "\n";
        }
        cin >> s;
    }
    return 0;
}