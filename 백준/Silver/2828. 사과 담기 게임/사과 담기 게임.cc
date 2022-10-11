#include <bits/stdc++.h>
using namespace std;

int n, m, j;
int l, r, ret;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> j;

    vector<int> v;
    for(int i = 0; i < j; i++){
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }

    l = 1, r = l + m;
    for(auto a : v){
        while(1){
            if(l <= a && a < r){
                break;
            }

            if(a < l){
                l--;
                r--;
                ret++;
            }
            else if(a >= r){
                l++;
                r++;
                ret++;
            }
        }
    }
    cout << ret;
    
    
    return 0;
}