#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    
    set<string> s;
    map<int, int> mp;
    
    bool flag = false;
    for(int i = 0; i < words.size(); i++){
        int p = i % n  + 1;
        mp[p]++;
        
        if(i > 0 && words[i-1].back() != words[i][0]){
            answer.push_back(p);
            answer.push_back(mp[p]);
            flag = true;
            break;
        }
        
        if(s.find(words[i]) != s.end()){
            answer.push_back(p);
            answer.push_back(mp[p]);
            flag = true;
            break;
        }
        s.insert(words[i]);
    }
    if(!flag){
        answer.push_back(0);
        answer.push_back(0);
    }

    return answer;
}