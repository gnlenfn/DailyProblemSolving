#include <bits/stdc++.h>

using namespace std;

int cntOne(int n){
    int cnt = 0;
    while(n){
        if(n % 2) cnt++;
        n /= 2;
    }
    return cnt;
}

int solution(int n) {
    int c = cntOne(n);
    while(1){
        n++;
        if(c == cntOne(n)) return n;
    }
}