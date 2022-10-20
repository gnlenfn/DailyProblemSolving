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
    
    // 입력되는 좌표와 인덱스 일치시켜야 함
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
        
        // 2개의 큐를 사용하는데, 
        // 기존의 bfs 용도와 같은 바깥의 큐 q : 여기서 처음으로 1을 만날때 까지 순회 반복
        // 쓰러트린 학생들을 저장하는 큐 --> 다음 점프 시에 큐의 초기값으로 사용
        // bfs순회 중 1을 만나면 그 칸을 0으로 바꾼 뒤 tmp에 저장하고
        // 0을 만나면 q에 저장하여 순회를 계속 반복
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
