#include <bits/stdc++.h>
using namespace std;

int n, m, ans;
map<int, vector<int>> mp;
int visited[505];
void bfs(int cur)
{
    fill(visited, visited + 504, -1); // -1로 모두 초기화
    queue<int> q;
    q.push(cur);
    visited[cur] = 0; // 시작 지점은 0

    while (!q.empty())
    {
        int x = q.front();
        q.pop();

        for (auto nxt : mp[x])
        {
            if (visited[nxt] != -1)
                continue;

            visited[nxt] = visited[x] + 1;
            if (visited[nxt] > 2)
                continue; // 1번 노드로부터 거리가 2보다 크면 카운트 안함

            q.push(nxt);
            ans++; // 거리가 2 이하인 노드 수만 카운트
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        mp[a].push_back(b);
        mp[b].push_back(a);
    }

    bfs(1);
    cout << ans << "\n";
    return 0;
}