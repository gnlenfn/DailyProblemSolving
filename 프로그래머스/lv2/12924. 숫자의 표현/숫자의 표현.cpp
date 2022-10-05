#include <bits/stdc++.h>

using namespace std;

int solution(int n) {
    int answer = 1;         // 절반 까지만 순회하는데, 1개로도 가능 (n 본인)
    int num = (n + 1) / 2;
    int sum = 0;
    int left = 1;
    
    for(int i = 1; i < num + 1; i++){
        sum += i;
        
        if(sum >= n){
            while(sum > n) sum -= left++;
            if(sum == n) answer++;
        }
    }
    return n == 1 ? 1 : answer;  // n이 1인 경우
}