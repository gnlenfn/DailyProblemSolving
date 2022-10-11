#include <bits/stdc++.h>
using namespace std;

int n, c, tmp, p;
map<int, pair<int, int>> mp;

bool cmp(const pair<int, pair<int, int>> &a, const pair<int, pair<int, int>> &b){
    if (a.second.first == b.second.first)
        return a.second.second < b.second.second;
    
    return a.second.first > b.second.first;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> c;
    for(int i = 0; i < n; i++){
        cin >> tmp;
        if(mp.find(tmp) != mp.end()){
            mp[tmp].first++;
        }
        else{
            mp[tmp] = {1, p};
            p++;
        }
    }
    vector<pair<int, pair<int, int>>> vec(mp.begin(), mp.end());
    sort(vec.begin(), vec.end(), cmp);
    for(auto elem : vec){
        // cout << elem.first << " :: " << elem.second.first << " " << elem.second.second << "\n";
        for(int i = 0; i < elem.second.first; i++){
            cout << elem.first << " ";
        }
    }
    return 0;
}