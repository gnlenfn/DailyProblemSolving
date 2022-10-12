#include <bits/stdc++.h>
using namespace std;

int n, m;
int grid[101][101];
int check[101][101];
const int dx[] = {-1, 1, 0, 0};
const int dy[] = {0, 0, 1, -1};
int count(int arr[101][101])
{
    int cnt = 0;

    for (int row = 0; row < n; row++)
    {
        for (int col = 0; col < m; col++)
        {
            if (arr[row][col] == 1)
                cnt++;
        }
    }
    return cnt;
}

void bfs()
{
    queue<pair<int, int>> q;
    memset(check, 0, sizeof(check));

    // (0,0) 부터 바깥쪽 공기층을 탐색
    // check에 바깥 공기층을 기록
    q.push({0, 0});
    check[0][0] = 1;

    int x, y;
    while (!q.empty())
    {
        tie(x, y) = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue; // grid 범위 바깥
            if (check[nx][ny])
                continue; // 이미 확인
            if (grid[nx][ny])
                continue; // 치즈인 경우

            check[nx][ny] = 1;
            q.push({nx, ny});
        }
    }

    // 바깥 공기와 닿은 치즈는 녹는다
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (grid[i][j] == 0)
                continue;

            for (int k = 0; k < 4; k++)
            {
                int ni = i + dx[k];
                int nj = j + dy[k];
                if (check[ni][nj])
                {
                    grid[i][j] = 0;
                    break;
                }
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> grid[i][j];
        }
    }

    int cheese = 0;
    int last = 0;
    int time = 0;
    while (1)
    {
        int tmp = count(grid);
        if (tmp == 0)
            break;
        else
            last = tmp;

        bfs();
        time++;
    }

    cout << time << "\n";
    cout << last << "\n";
    return 0;
}