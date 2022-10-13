#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer = {0, 0};
    int n = sqrt(yellow + brown) + 1;
    
    for(int i = 1; i < n + 1; i++){
        if((yellow + brown) % i == 0){
            int w = (yellow + brown) / i;
            int h = i;
            if((w - 2) * (h - 2) == yellow){
                answer[0] = w;
                answer[1] = h;
            }
        }
    }
    sort(answer.begin(), answer.end(), greater<int>());
    return answer;
}