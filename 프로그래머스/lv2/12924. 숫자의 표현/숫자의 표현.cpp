#include <bits/stdc++.h>

using namespace std;

int solution(int n) {
    int answer = 0;
    int left = 0, right = 0;
    vector<int> v;
    for(int i = 1; i <= n; i++) v.push_back(i);
    
    while(left < n){
        int sum = accumulate(v.begin() + left, v.begin() + right, 0);
        if(sum == n){
            answer++;
            left++;
            right++;
        }
        else if(sum > n) left++;
        else if(sum < n) right++;
    }
    return answer;
}