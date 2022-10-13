#include <bits/stdc++.h>

using namespace std;


vector<int> answer = {0, 0};

string bin(int n){
    string ret;
    while(n){
        ret += to_string(n % 2);
        n /= 2;
    }
    reverse(ret.begin(), ret.end());
    return ret;
}
vector<int> solution(string s) {  
    answer[0]++;
    string ret = "";

    for(char c : s){
        if(c == '1') ret += c;
        else answer[1]++;
    }
    if(ret == "1"){
        return answer;
    }
    string num = bin(ret.size());
    
    return solution(num);
}