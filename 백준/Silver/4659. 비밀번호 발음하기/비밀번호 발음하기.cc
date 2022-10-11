#include <bits/stdc++.h>
using namespace std;

string p;

bool vowelCheck(char c){
    return (c == 'a' || c == 'e' || c == 'i' || c =='o' || c == 'u');
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    while(cin >> p){
        int vcnt = 0, ccnt = 0;
        bool noV = true;
        bool state = true;
        if(p == "end") break;

        for(int i = 0; i < p.size(); i++){

            if(vowelCheck(p[i])){
                ccnt = 0;
                vcnt++;
                noV = false;
            }
            else{
                ccnt++;
                vcnt = 0;
            } 

            if(vcnt > 2 || ccnt > 2){
                state = false; // not accept
                break;
            } 
            
            if(i > 0 && p[i] == p[i-1] && (p[i] != 'e' && p[i] != 'o')){
                state = false;
                break;
            }

        }
        if(noV) state = false;
        if(state) cout << '<' << p << '>' << " is acceptable." << "\n";
        else cout << '<' << p << '>' << " is not acceptable." << "\n";

    }
    return 0;
}    
