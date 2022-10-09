#include <bits/stdc++.h>
using namespace std;

int T, n, m, K, x, y;
const int dx[] = {1, -1, 0, 0};
const int dy[] = {0, 0, 1, -1};
int arr[51][51];
int visited[51][51];
int ret;

void dfs(int row, int col){
    visited[row][col] = 1;
    for(int i = 0; i < 4; i++){
        int nx = row + dx[i];
        int ny = col + dy[i];

        if(0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && arr[nx][ny] == 1)
            dfs(nx, ny);

    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> T;
    for(int t = 0; t < T; t++){
        cin >> m >> n >> K;

        fill(&arr[0][0], &arr[0][0] + 51 * 51, 0);
        fill(&visited[0][0], &visited[0][0] + 51 * 51, 0);
        for(int k = 0; k < K; k++){
            cin >> y >> x;
            arr[x][y] = 1;
        }

        ret = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(!visited[i][j] && arr[i][j] == 1){
                    dfs(i, j);
                    ret++; 
                }
                    
                
            }
        }

        cout << ret << "\n";
    }
    
    return 0;
}