#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b){
    if(b == 0) return a;
    else return gcd(b, a % b);
}

int solution(vector<int> arr) {
    int answer = 0;
    
    int tmp = 1;
    for(int i = 0; i < arr.size(); i++){
        tmp = tmp * arr[i] / gcd(tmp, arr[i]);
    }
    return tmp;
}