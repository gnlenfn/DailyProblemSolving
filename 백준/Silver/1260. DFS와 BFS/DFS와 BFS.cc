#include <bits/stdc++.h>
using namespace std;

int m, n, v;
vector<int> vec[1005];
vector<int> bfs_ret;
vector<int> dfs_ret;
int visited[1005];
queue<int> q;

void dfs(int cur)
{
    visited[cur] = 1;
    dfs_ret.push_back(cur);

    for (int i = 0; i < vec[cur].size(); i++)
    {
        if (!visited[vec[cur][i]])
        {
            dfs(vec[cur][i]);
        }
    }
}

void bfs()
{
    cout << "\n";
    int visited[1005];
    memset(visited, 0, sizeof(visited));

    q.push(v);
    visited[v] = 1;
    bfs_ret.push_back(v);

    while (!q.empty())
    {
        int cur;
        tie(cur) = q.front();
        q.pop();

        for (int i = 0; i < vec[cur].size(); i++)
        {
            if (!visited[vec[cur][i]])
            {
                q.push(vec[cur][i]);
                visited[vec[cur][i]] = 1;
                bfs_ret.push_back(vec[cur][i]);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m >> v;

    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        vec[a].push_back(b);
        vec[b].push_back(a);
    }

    for (int i = 1; i <= n; i++)
    {
        sort(vec[i].begin(), vec[i].end());
    }

    dfs(v);
    for (int ver : dfs_ret)
    {
        cout << ver << " ";
    }
    bfs();
    for (int ver : bfs_ret)
    {
        cout << ver << " ";
    }
    return 0;
}