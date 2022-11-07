#include <bits/stdc++.h>
using namespace std;

long long n, x;
vector<long long> v;
int cnt;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++){
        long long tmp;
        cin >> tmp;
        v.push_back(tmp);
    }
    cin >> x;

    sort(v.begin(), v.end());
    int l = 0, r = v.size() - 1;
    while(l < r){
        if(v[l] + v[r] == x){
            cnt++;
            l++;
            r--;
        }
        else if(v[l] + v[r] < x) l++;
        else if(v[l] + v[r] > x) r--;
    }

    cout << cnt << "\n";
    
    return 0;
}