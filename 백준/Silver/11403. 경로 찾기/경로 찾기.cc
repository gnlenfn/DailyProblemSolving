#include <bits/stdc++.h>
using namespace std;

int n;
int mat[101][101];
int visited[101];

void bfs(int node)
{
    // BFS로 현재 노드에서 방문할 수 있는 다른 모든 노드 체크
    // row별로 방문할 수 있는지 확인한다

    queue<int> q;
    q.push(node);
    fill(begin(visited), end(visited), 0); // visited 초기화 -> row별로 체크함
    while (!q.empty())
    {
        int x = q.front();
        q.pop();

        for (int y = 1; y <= n; y++)
        {
            if (mat[x][y] == 0 || visited[y])
                continue;
            visited[y] = 1;
            q.push(y);
        }
    }

    /// visited true이면 갈 수 있음, false면 갈 수 없음
    for (int i = 1; i <= n; i++)
    {
        cout << (visited[i] ? 1 : 0) << " ";
    }
    cout << "\n";
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cin >> mat[i][j]; // 인접행렬 입력받기
        }
    }

    for (int i = 1; i <= n; i++)
    {
        bfs(i);
    }

    return 0;
}