#include <bits/stdc++.h>

using namespace std;

int dp[100001];
int solution(int n) {

    dp[0] = 0;
    dp[1] = 1;
    
    for(int i = 2; i < n + 1; i++){
        dp[i] = (dp[i-2] + dp[i-1]) % 1234567;
    }
    
    return dp[n];
}