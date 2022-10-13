#include <bits/stdc++.h>
using namespace std;

int n, m;
int a, b;
vector<int> v[10001];
int result[10001];
int visited[10001];
int dp[10001];
int mx;
// 현재 맥스값 보다 이번 카운트가 더 크면
// 정답 리스트 초기화 & push
// 맥스값과 같으면
// 그냥 push
// 작으면 pass
int dfs(int n)
{
    visited[n] = 1;
    int ret = 1;
    for (auto node : v[n])
    {
        if (!visited[node])
            ret += dfs(node);
    }
    return ret;
}
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    
    cin >> n >> m;
    while (m--)
    {
        cin >> a >> b;
        v[b].push_back(a);
    }

    for (int i = 0; i <= n; i++)
    {
        memset(visited, 0, sizeof(visited));
        dp[i] = dfs(i);
        mx = max(dp[i], mx);
    }

    for (int i = 0; i <= n; i++)
    {
        if (dp[i] == mx)
        {
            cout << i << " ";
        }
    }
    return 0;
}