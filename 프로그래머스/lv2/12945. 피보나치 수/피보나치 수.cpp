#include <bits/stdc++.h>
using namespace std;

int dp[100001];

int fibo(int n) {
    if(dp[n]){
        return dp[n];
    } 
    
    if (n == 1) return 1;
    if (n == 0) return 0;
    
    dp[n] = (fibo(n-2) + fibo(n-1)) % 1234567;
    
    return dp[n];
}
int solution(int n) {
    
    return fibo(n);

}