#include <bits/stdc++.h>
using namespace std;

int n, m;
int row, col;
int mat[505][505];
int visited[505][505];
int dx[] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[] = {2, 1, -1, -2, 2, 1, -1, -2};
void bfs()
{
    fill(&visited[0][0], &visited[0][0] + 504 * 504, -1);  // -1로 초기화 -> 시작점을 0으로 만들기 위해
    queue<pair<int, int>> q;
    q.push({row, col});
    visited[row][col] = 0;

    while (!q.empty())
    {
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for (int i = 0; i < 8; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 1 || nx > n || ny < 1 || ny > n)
                continue; // 좌표 1부터 시작, 좌표 범위 초과
            if (visited[nx][ny] != -1)
                continue; // 이미 방문

            visited[nx][ny] = visited[x][y] + 1;
            q.push({nx, ny});
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    cin >> row >> col;        // 나이트 위치
    vector<pair<int, int>> v; // target 위치 저장
    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        v.push_back({x, y});
    }

    bfs();

    for (auto c : v)
    {
        cout << visited[c.first][c.second] << " ";
    }
    return 0;
}