#include <bits/stdc++.h>
using namespace std;

int n;
int t[3];
int hp[61][61][61];
int visited[61][61][61];
int cases[6][3] = {
    {9, 3, 1},
    {9, 1, 3},
    {3, 9, 1},
    {3, 1, 9},
    {1, 9, 3},
    {1, 3, 9}
};
struct tmp{
    int a, b, c;
};

queue<tmp> qq;
int solv(int x, int y, int z){
    
    qq.push({x, y, z});
    visited[x][y][z] = 1;

    while(!qq.empty()){
        int p = qq.front().a;
        int q = qq.front().b;
        int r = qq.front().c;
        qq.pop();

        if(visited[0][0][0]) break; // [0][0][0]이 모든 값이 0이 되는 곳

        for(int i = 0; i < 6; i++){
            int np = max(0, p - cases[i][0]);
            int nq = max(0, q - cases[i][1]);
            int nr = max(0, r - cases[i][2]);

            if(visited[np][nq][nr]) continue;

            visited[np][nq][nr] = visited[p][q][r] + 1;
            qq.push({np, nq, nr});
        }
    }
    return visited[0][0][0] - 1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> t[i];
    }

    cout << solv(t[0], t[1], t[2]) << "\n";
    return 0;
}