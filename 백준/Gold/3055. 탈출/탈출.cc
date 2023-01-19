#include <bits/stdc++.h>
using namespace std;

int r, c;
char mat[51][51];
int dist[51][51];
int waterDist[51][51];
int visited[51][51];
pair<int, int> dest;

int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

void flood()
{
    fill(&waterDist[0][0], &waterDist[0][0] + 51 * 51, -1);
    queue<pair<int, int>> q;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (mat[i][j] == '*')
            {
                q.push({i, j});      // 물인 칸 큐에 넣기
                waterDist[i][j] = 0; // 물 시작 거리 0
                visited[i][j] = 1;   // 물 방문 했나 안했나 확인
            }
        }
    }

    while (q.size())
    {
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= r || ny < 0 || ny >= c)
                continue; // 좌표 범위 초과
            if (mat[nx][ny] != '.')
                continue; // 물이 넘칠 수 있는 칸은 .인 빈칸 뿐
            if (visited[nx][ny])
                continue; // 이미 방문한 곳은 패스

            waterDist[nx][ny] = waterDist[x][y] + 1;
            q.push({nx, ny});
            visited[nx][ny] = 1;
        }
    }
}

void move()
{
    fill(&dist[0][0], &dist[0][0] + 51 * 51, -1);
    queue<pair<int, int>> q;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            visited[i][j] = 0; // visited 위에서 물 이동때 사용한 것 재사용하기 위해 모두 0으로 초기화하는 줄
            if (mat[i][j] == 'S')
            { // 시작점 찾기
                q.push({i, j});
                dist[i][j] = 0;
                visited[i][j] = 1;
            }
            else if (mat[i][j] == 'D')
            {
                dest = {i, j};
            }
        }
    }

    while (q.size())
    {
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= r || ny < 0 || ny >= c)
                continue; // 좌표 범위 초과
            if (mat[nx][ny] != '.' and mat[nx][ny] != 'D')
                continue; // 물이 넘칠 수 있는 칸은 .인 빈칸 뿐, 도착점은 가야함
            if (waterDist[nx][ny] != -1 && waterDist[nx][ny] <= dist[x][y] + 1)
                continue; // 물에 잠긴 곳 혹은 다음 턴에 물에 잠길 곳은 패스
            if (visited[nx][ny])
                continue; // 방문한 곳 다시 안가기

            dist[nx][ny] = dist[x][y] + 1;
            q.push({nx, ny});
            visited[nx][ny] = 1;
        }
    }
}

void getInput()
{
    cin >> r >> c;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> mat[i][j];
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    getInput();

    flood();
    move();

    if (dist[dest.first][dest.second] != -1)
    {
        cout << dist[dest.first][dest.second] << "\n";
    }
    else
    {
        cout << "KAKTUS"
             << "\n";
    }
    return 0;
}