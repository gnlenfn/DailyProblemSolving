#include <bits/stdc++.h>

using namespace std;

bool check(string s){
    map<char, char> mp = {{'}', '{'}, {')', '('}, {']', '['}};
    stack<char> stk;
    string a = "([{";
    for(auto p : s){
        if (a.find(p) != string::npos) stk.push(p);
        else if(!stk.empty() && stk.top() == mp[p]) stk.pop();
        else stk.push(p);
    }
    if(stk.empty()) return 1;
    return 0;
}

int solution(string s) {
    int answer = 0;
    
    for(int i = 0; i < s.length(); i++){
        rotate(s.begin(), s.begin() + 1, s.end());
        if(check(s)) answer++;

    }
    return answer;
}