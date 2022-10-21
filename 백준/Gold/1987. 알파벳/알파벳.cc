#include <bits/stdc++.h>
using namespace std;

int r, c, ret;
char arr[21][21];
int visited[30];
int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
void dfs(int x, int y, int cnt)
{
    ret = max(ret, cnt);
    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= r || ny >= c)
            continue; // 범위 초과
        int num = (int) arr[nx][ny] - 'A';
        
        if (visited[num] == 0){
            visited[num] = 1;
            dfs(nx, ny, cnt + 1);
            visited[num] = 0;           
        }

    }
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> r >> c;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> arr[i][j];
        }
    }

    visited[(int) arr[0][0] - 'A'] = 1;
    dfs(0, 0, 1);

    cout << ret << "\n";

    return 0;
}