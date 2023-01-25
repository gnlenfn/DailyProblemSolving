#include <bits/stdc++.h>
using namespace std;

int n, m;                 // 컴퓨터수 n, 간선 수 m
map<int, vector<int>> mp; // 그래프
int visited[105];

void dfs(int computer)
{
    visited[computer] = 1;

    for (auto node : mp[computer])
    {
        if (!visited[node])
        {
            dfs(node);
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;

    // 네트워크 구성 그리기
    for (int i = 0; i < m; i++)
    {
        int a, b;
        cin >> a >> b;
        mp[a].push_back(b);
        mp[b].push_back(a);
    }

    dfs(1); // 1번 컴퓨터가 감염될 때 감염될 전체 컴퓨터 수 구하기 -> 시작점이 1
    int ans = 0;
    for (int i : visited)
    {
        ans += i;
    }

    cout << ans - 1 << "\n"; // 1번 컴퓨터에 의해 감염되는 수 이므로 1번은 제외
    return 0;
}