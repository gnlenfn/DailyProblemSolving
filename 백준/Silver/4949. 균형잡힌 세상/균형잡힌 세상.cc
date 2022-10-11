#include <bits/stdc++.h>
using namespace std;

string sent;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    while(getline(cin, sent)){
        bool check = true;
        if(sent == ".") break;
        
        stack<char> stk;
        for(auto c : sent){
            if(c == '(' || c == '[') stk.push(c);

            else if(c == ')'){
                if(!stk.empty() && stk.top() == '(') stk.pop();
                else{
                    check = false;
                    break;
                }
            }
            
            else if(c == ']'){
                if(!stk.empty() && stk.top() == '[') stk.pop();
                else{
                    check = false;
                    break;
                }
            }
        }
        if(!stk.empty() || !check) cout << "no" << "\n";
        else cout << "yes" << "\n";
    }
    return 0;
}