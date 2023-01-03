#include <bits/stdc++.h>
using namespace std;

int n, l, r, sum, cnt;
int grid[51][51];
int visited[51][51];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
vector<pair<int, int>> v;

void dfs(int row, int col, vector<pair<int, int>> &v)
{
    // row, col은 이번에 방문하는 곳 좌표
    // v는 지금까지 방문헀던 좌표 기록하는 벡터
    // grid 범위 안에서 l이상 r이하 차이가 나는 곳들의 모든 합을 구함 -> sum
    // sum을 v의 길이로 나누면 인구 이동 후 같아질 인구
    for (int i = 0; i < 4; i++)
    {
        int nr = row + dx[i];
        int nc = col + dy[i];
        int sub = abs(grid[nr][nc] - grid[row][col]);

        if (nr < 0 || nc < 0 || nr >= n || nc >= n)
            continue;
        if (visited[nr][nc])
            continue;
        if (sub > r || sub < l)
            continue;

        visited[nr][nc] = 1;
        v.push_back({nr, nc});
        sum += grid[nr][nc];
        dfs(nr, nc, v);
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> l >> r;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> grid[i][j];
        }
    }

    // visited를 초기화
    // 모든 칸을 탐색
    // dfs함수 종료되면 방문한 좌표들은 모두 계산된 인구로 변화
    // 인구이동이 일어날 때 마다 cnt++

    while (true)
    {
        bool flag = 0;
        fill(&visited[0][0], &visited[0][0] + 51 * 51, 0); // visited 초기화
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!visited[i][j]) // 새로 방문하는 점
                {
                    v.clear(); // 방문한 점 기록하는 벡터 초기화
                    visited[i][j] = 1;
                    sum = grid[i][j];
                    v.push_back({i, j});
                    dfs(i, j, v);

                    if (v.size() == 1)
                        continue;
                    for (pair<int, int> p : v)
                    {
                        grid[p.first][p.second] = sum / v.size();
                        flag = 1; // 인구이동 있었음 표시
                    }
                }
            }
        }
        if (!flag)
            break; // 더이상 이동이 없으면 끝
        cnt++;
    }

    cout << cnt;
    return 0;
}