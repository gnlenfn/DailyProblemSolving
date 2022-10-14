#include <bits/stdc++.h>
using namespace std;

int n, m;
int grid[51][51];

// 2차원 배열의 최댓값 찾기
int findMax(int arr[51][51])
{
    int mx = INT_MIN;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            mx = max(mx, arr[i][j]);
        }
    }

    return mx;
}

// bfs로 최단거리 찾기 실행
// 그리고 findMax 함수를 통해 가장 먼 거리 반환
int bfs(int row, int col)
{
    if (grid[row][col] == 'W')
        return -1;
    queue<pair<int, int>> q;
    int visited[51][51];
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    fill(&visited[0][0], &visited[0][0] + 51 * 51, -1);
    q.push({row, col});
    visited[row][col] = 0;

    while (!q.empty())
    {
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue;
            if (visited[nx][ny] >= 0 || grid[nx][ny] == 'W')
                continue;

            visited[nx][ny] = visited[x][y] + 1;
            q.push({nx, ny});
        }
    }

    return findMax(visited);
}

int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < m; j++)
        {
            grid[i][j] = tmp[j];
        }
    }

    int mx = INT_MIN;
    // 주어진 grid의 모든 점을 탐색하며 가장 먼 두 점간의 거리 찾기
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            mx = max(mx, bfs(i, j));
        }
    }

    cout << mx << "\n";
    return 0;
}