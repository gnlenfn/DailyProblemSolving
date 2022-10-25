#include <bits/stdc++.h>
using namespace std;

int r, c, k, ret;
char arr[6][6];
int visited[6][6];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int dfs(int row, int col)
{
    if (row == 0 && col == c - 1)
    {
        if (k == visited[row][col])
            return 1;
        return 0;
    }
    int ret = 0;
    for (int i = 0; i < 4; i++)
    {
        int nx = row + dx[i];
        int ny = col + dy[i];

        if (nx < 0 || ny < 0 || nx >= r || ny >= c || visited[nx][ny])
            continue;
        if (arr[nx][ny] == 'T')
            continue;

        visited[nx][ny] = visited[row][col] + 1;
        ret += dfs(nx, ny);
        visited[nx][ny] = 0;
    }
    return ret;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> r >> c >> k;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> arr[i][j];
        }
    }

    visited[r - 1][0] = 1;
    cout << dfs(r - 1, 0);

    return 0;
}