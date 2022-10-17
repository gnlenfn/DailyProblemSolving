#include <bits/stdc++.h>
using namespace std;

int n, k, ret;
int visited[200001];
int prev_p[200001]; 
vector<int> v;
int cnt;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> k;
    
    queue<int> q;
    visited[n] = 1;
    q.push(n);

    while(q.size()){
        int here = q.front();
        q.pop();

        if(here == k){
            ret = visited[k];
            break;
        }
        for(int next_p : {here + 1, here - 1, here * 2}){
            if(next_p >= 200001 || next_p < 0 || visited[next_p]) continue;

            visited[next_p] = visited[here] + 1;
            q.push(next_p);
            prev_p[next_p] = here;
        }
    }
    for(int i = k; i != n; i = prev_p[i]){
        v.push_back(i);
    }
    v.push_back(n);

    cout << ret - 1 << "\n";
    reverse(v.begin(), v.end());
    for(int i : v) cout << i << " ";

    return 0;
}