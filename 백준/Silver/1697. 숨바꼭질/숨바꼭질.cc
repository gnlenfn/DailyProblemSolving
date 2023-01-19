#include <bits/stdc++.h>
using namespace std;

int n, k;
int visited[200005];

int bfs(int start)
{

    queue<int> q;
    q.push(start);
    visited[start] = 0;

    while (!q.empty())
    {
        int cur = q.front();
        q.pop();
        if (cur == k)
            break;

        int move[] = {cur + 1, cur - 1, 2 * cur};
        for (int i = 0; i < 3; i++)
        {
            int nxt = move[i];
            if (visited[nxt] != -1)
                continue;
            if (nxt > 100000)
                continue;

            visited[nxt] = visited[cur] + 1;
            q.push(nxt);
        }
    }

    return visited[k];
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> k;

    fill(visited, visited + 200001, -1);
    cout << bfs(n) << "\n";

    return 0;
}