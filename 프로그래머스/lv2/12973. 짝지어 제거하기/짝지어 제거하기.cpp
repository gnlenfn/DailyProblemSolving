#include <bits/stdc++.h>
using namespace std;

int solution(string s)
{
    stack<char> stk;
    
    for(char c : s){
        if(!stk.empty() && stk.top() == c) stk.pop();
        else stk.push(c);
    }
    
    if(!stk.empty()) return 0;
    return 1;
}