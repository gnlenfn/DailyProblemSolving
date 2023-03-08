#include <bits/stdc++.h>
using namespace std;

int graph[304][304], visited[304][304];
int n, m, land, year, ans;
int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

void dfs(int row, int col)
{
    visited[row][col] = 1;
    for (int i = 0; i < 4; i++)
    {
        int nx = row + dx[i];
        int ny = col + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m)
            continue;
        if (graph[nx][ny] == 0)
            continue;
        if (visited[nx][ny])
            continue;

        dfs(nx, ny);
    }
}

tuple<int, int, int> count_water(int row, int col)
{
    int cnt = 0;
    for (int i = 0; i < 4; i++)
    {
        int nx = row + dx[i];
        int ny = col + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m)
            continue;
        if (graph[nx][ny] == 0)
        {
            cnt++;
        }
    }

    return make_tuple(row, col, cnt);
}

int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                cin >> graph[i][j];
            }
        }

    land = 1;
    while (land == 1)
    {
        land = 0;
        memset(visited, 0, sizeof(visited));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (visited[i][j] == 0 && graph[i][j] > 0)
                {
                    dfs(i, j);
                    land++;
                }
            }
        }
        if (land > 1)
        {
            cout << year << "\n";
            return 0;
        }
        queue<tuple<int, int, int>> melt;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (graph[i][j] != 0)
                {
                    melt.push(count_water(i, j));
                }
            }
        }
        while (!melt.empty())
        {
            int row, col, c;
            tie(row, col, c) = melt.front();
            melt.pop();

            graph[row][col] -= c;
            if (graph[row][col] < 0)
            {
                graph[row][col] = 0;
            }
        }
        year++;
    }

    cout << ans << "\n";
    return 0;
}