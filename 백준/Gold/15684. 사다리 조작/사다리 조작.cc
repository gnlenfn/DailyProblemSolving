#include <bits/stdc++.h>
using namespace std;

int n, m, h, ret = INT_MAX;
int grid[33][13];

bool check(){
    for(int i = 1; i <= n; i++){
        int start = i;
        for(int j = 1; j <= h; j++){
            if(grid[j][start]) start++;
            else if(grid[j][start-1]) start--;
        }
        if(start != i) return false;
    }
    return true;
}

void go(int here, int cnt){
    if(cnt > 3) {
        return;
    }
    if(check()){
        ret = min(ret, cnt);
        return;
    } 

    for(int i = here; i <= h; i++) {
        for(int j = 1; j <= n; j++){
            if(grid[i][j] || grid[i][j-1] || grid[i][j+1]) continue;

            grid[i][j] = 1;
            go(i, cnt + 1);
            grid[i][j] = 0;
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> h;
    for(int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        grid[a][b] = 1;
    }   

    go(1, 0);
    cout << ((ret == INT_MAX) ? -1 : ret) << "\n";
    return 0;
}