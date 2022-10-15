#include <bits/stdc++.h>
using namespace std;

int n, l, r, cnt, sum;
int grid[51][51];
int visited[51][51];
vector<pair<int, int>> v;
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
void dfs(int row, int col, vector<pair<int, int>> &v){
    // dfs 순회 하면서 국경열린 곳 인구 모두 더하기
    // 인접한 두 칸의 인구 차이가 l <= p <= r이면 개방
    for(int i = 0; i < 4; i++){
        int nr = row + dx[i];
        int nc = col + dy[i];
        int sub = abs(grid[row][col] - grid[nr][nc]);

        if(nr < 0 || nc < 0 || nr >= n || nc >= n) continue;
        if(visited[nr][nc] == 1) continue;
        if(sub > r || sub < l) continue;

        visited[nr][nc] = 1;
        v.push_back({nr, nc}); // 이번 카운트에 방문한 칸
        sum += grid[nr][nc];
        dfs(nr, nc, v);
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> l >> r;
    // 초기값 입력
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> grid[i][j];
        }
    }

    // 모든 칸을 탐색
    // dfs함수 종료되면 visited 1인 칸을 찾아 gird에 인구 평균 입력
    // 이때 cnt++
    // visited 초기화 
    while (1)
    {
        bool flag = 0;
        fill(&visited[0][0], &visited[0][0] + 51 * 51, 0);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(!visited[i][j]){
                    v.clear();
                    visited[i][j] = 1;
                    sum = grid[i][j];    // 첫 칸에서 시작하므로 sum값도 미리더해줘
                    v.push_back({i, j}); // 여기도 마찬가지
                    dfs(i, j, v);

                    // 인구이동 적용
                    if(v.size() == 1) continue;
                    for(pair<int, int> n : v){
                        grid[n.first][n.second] = sum / v.size();
                        flag = 1;
                    }  
                }
            }
        }
        if(!flag) break; // 더이상 이동 못하면 종료
        cnt++;
    }
    
    cout << cnt << "\n";
    return 0;
}