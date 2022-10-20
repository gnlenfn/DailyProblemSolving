#include <bits/stdc++.h>
using namespace std;

int n, m, r1, c1, r2, c2;
char arr[303][303];
int visited[303][303];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> r1 >> c1 >> r2 >> c2;
    for (int i = 0; i < n; i++)
    {
        string tmp;
        cin >> tmp;
        for (int j = 0; j < m; j++)
        {
            arr[i][j] = tmp[j];
        }
    }

    r1--;
    r2--;
    c1--;
    c2--;
    queue<pair<int, int>> q;
    q.push({r1, c1});
    visited[r1][c1] = 1;

    int cnt = 0;
    while (arr[r2][c2] != '0')
    {
        cnt++;
        queue<pair<int, int>> tmp;

        while (q.size())
        {
            int x, y;
            tie(x, y) = q.front();
            q.pop();

            int dx[] = {1, -1, 0, 0};
            int dy[] = {0, 0, 1, -1};
            for (int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m || visited[nx][ny])
                    continue;
                visited[nx][ny] = cnt;
                if (arr[nx][ny] != '0')
                {
                    arr[nx][ny] = '0';
                    tmp.push({nx, ny});
                }
                else
                    q.push({nx, ny});
            }
        }

        q = tmp;
    }

    cout << visited[r2][c2] << "\n";

    return 0;
}