#include <bits/stdc++.h>
using namespace std;

int n, visited[100004];
long long cnt;
vector<int> v;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++){
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }
    
    int l = 0, r = 0;
    for(l; l < n; l++){
        while(r < n) {
            if(visited[v[r]]) break;
            visited[v[r]] = 1;
            r++;
        }
        cnt += (r - l);
        visited[v[l]] = 0;
    }

    cout << cnt << "\n";
    return 0;
}