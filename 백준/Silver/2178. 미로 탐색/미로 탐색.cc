#include <bits/stdc++.h>
using namespace std;

int n, m;
int mat[105][105];
int visited[105][105];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void bfs(int row, int col)
{
    queue<pair<int, int>> q;
    q.push({row, col}); // 시작 좌표 입력, 이 문제는 (1, 1) 고정
    visited[row][col] = 1;

    while (!q.empty())
    {
        int x, y;
        tie(x, y) = q.front();
        q.pop(); // 큐 맨 앞 꺼내기

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i]; // (x, y)에서 네 방향 이동 수행

            if (nx < 1 || nx > n || ny < 1 || ny > m)
                continue; // 좌표 범위 초과
            if (visited[nx][ny] != 0 || mat[nx][ny] == 0)
                continue; // 이미 방문했거나 이동할 수 없는 칸

            visited[nx][ny] = visited[x][y] + 1; // 방문처리 및 최단거리 기록
            q.push({nx, ny});                    // 방문 예정 큐로 추가
        }
    }
}

int main()
{

    cin >> n >> m;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            scanf("%1d", &mat[i][j]);
        }
    }

    bfs(1, 1);
    cout << visited[n][m] << endl;
    return 0;
}