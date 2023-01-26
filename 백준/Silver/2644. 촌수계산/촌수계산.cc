#include <bits/stdc++.h>
using namespace std;

int n, a, b, m;
map<int, vector<int>> mp;
int visited[104];

void bfs(int start)
{
    queue<int> q;
    q.push(start);
    fill(visited, visited + 102, -1);
    visited[start] = 0;

    while (!q.empty())
    {
        int cur = q.front();
        q.pop();

        for (int node : mp[cur])
        {
            if (visited[node] == -1)
            {
                q.push(node);
                visited[node] = visited[cur] + 1;
            }
        }
    }
}

int main()
{
    // 촌수계산 할 때 노드 이동 마다 1촌씩 증가 -> BFS 최단거리 문제
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> a >> b >> m; // a 친척 수, a,b 촌수 계산할 두 명
    for (int i = 0; i < m; i++)
    {
        int x, y;
        cin >> x >> y;
        mp[x].push_back(y);
        mp[y].push_back(x); // 무방향 그래프
    }

    bfs(a);
    cout << visited[b] << "\n";

    return 0;
}