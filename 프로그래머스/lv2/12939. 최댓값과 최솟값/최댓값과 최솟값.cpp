#include <bits/stdc++.h>

using namespace std;

string solution(string s) {
    string answer = "", token = "";
    vector<int> v;
    int min = 0, max = 0;
    
    for(stringstream str(s); str >> token;){
        v.push_back(stoi(token));
    }
    sort(v.begin(), v.end());
    answer += to_string(v.front()) + " " + to_string(v.back());
    
    return answer;
}