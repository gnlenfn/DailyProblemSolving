#include <bits/stdc++.h>
using namespace std;

int n, g[11][11], visited[11][11], ret = INT_MAX;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int check(int row, int col)
{
    // 꽃을 심을 수 있는지 check
    if (visited[row][col])
        return 0;

    for (int i = 0; i < 4; i++)
    {
        int nr = row + dx[i];
        int nc = col + dy[i];
        if (nr < 0 || nc < 0 || nr >= n || nc >= n || visited[nr][nc])
            return 0;
    }
    return 1;
}

int setFlower(int row, int col)
{
    // 꽃 심기, return cost
    visited[row][col] = 1;
    int c = g[row][col];
    for (int i = 0; i < 4; i++)
    {
        int nx = row + dx[i];
        int ny = col + dy[i];

        visited[nx][ny] = 1;
        c += g[nx][ny];
    }
    return c;
}

void eraseFlower(int row, int col)
{
    // 꽃 지우기
    visited[row][col] = 0;
    for (int i = 0; i < 4; i++)
    {
        int nx = row + dx[i];
        int ny = col + dy[i];

        visited[nx][ny] = 0;
    }
}

void go(int cnt, int cost)
{ // cnt -> 심은 갯수, cost -> 비용
    if (cnt == 3)
    {
        ret = min(ret, cost);
        return;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (check(i, j))
            {
                go(cnt + 1, cost + setFlower(i, j));
                eraseFlower(i, j);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> g[i][j];
        }
    }

    go(0, 0);
    cout << ret << "\n";

    return 0;
}