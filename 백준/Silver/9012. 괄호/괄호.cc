#include <bits/stdc++.h>
using namespace std;

string p;
int t;

bool check(string str){
    stack<char> stk;
    for(auto p : str){
        if(p == '(') stk.push(p);
        else{
            if(!stk.empty()) stk.pop();
            else 
                return false;
        }
    }
    if(stk.empty())
        return true;
    else
        return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> t;
    for(int i = 0; i < t; i++){
        cin >> p;
        if(check(p)) cout << "YES" << "\n";
        else cout << "NO" << "\n";
    }
    return 0;
}