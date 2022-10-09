#include <bits/stdc++.h>
using namespace std;

int n, m, k;
int ax, ay, bx, by;
vector<int> ret;
int cnt;
int arr[101][101];
int visited[101][101];

const int dx[] = {1, -1, 0, 0};
const int dy[] = {0, 0, 1, -1};
int dfs(int x, int y, int cnt){
    visited[x][y] = 1;
    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && arr[nx][ny] == 1){
            cnt = dfs(nx, ny, cnt + 1);
        }
    }

    return cnt;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> k;

    fill(&arr[0][0], &arr[0][0] + 101 * 101, 1);
    for(int i = 0; i < k; i++){
        cin >> ax >> ay >> bx >> by;
        for(int q = min(ay, by); q < max(ay, by); q++){
            for(int p = min(ax, bx); p < max(ax, bx); p++)
                arr[q][p] = 0;
        }
    }

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(!visited[i][j] && arr[i][j] == 1){
                cnt = dfs(i, j, 1);
                ret.push_back(cnt);
            }
        }
    }

    cout << ret.size() << "\n";
    sort(ret.begin(), ret.end());
    for(auto r : ret) cout << r << " ";
    
    return 0;
}