#include <bits/stdc++.h>
using namespace std;

bool solution(string s)
{
    stack<char> stk;
    for(auto p : s){
        if(p == '(') stk.push(p);
        else if(!stk.empty() && stk.top() == '('){
            stk.pop();
        }            
        else return false;
    }
    if(!stk.empty()) return false;

    return true;
}