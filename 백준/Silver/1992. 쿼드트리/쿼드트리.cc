#include <bits/stdc++.h>
using namespace std;
int n;
vector<vector<char>> graph;

int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

string quart(int y, int x, int size) {
    char valid = graph[y][x];
    string ret = "";
    for(int i= y; i< y+ size; i++) {
        for(int j=x; j<x+ size; j++) {
            if(valid != graph[i][j]) {
                ret += "(";
                ret += quart(y, x, size /2);
                ret += quart(y, x + size/2 , size/2);
                ret += quart(y+ size/2, x, size/2);
                ret += quart(y+ size/2, x + size/2, size/2);
                ret += ")";
                return ret;
            }
        }
    }
    return string(1,valid);
}
int main() {
    // 그래프를 1/4토막
    // 이게 전부 0이거나 전부 1이면 통과 (0  or 1)
    // 아니면 다시 1/4토막
    // 결과가 나올 때 까지 반복
    // 쿼드트리 만들기

    cin >> n;
    graph.assign(n, vector<char>(n));
    for (int i =0; i<n; i++) {
        string s;
        cin >> s;
        for (int j =0; j<n; j++) {
            graph[i][j] = s[j];
        }
    }

    cout << quart(0,0,n);
    return 0;
}