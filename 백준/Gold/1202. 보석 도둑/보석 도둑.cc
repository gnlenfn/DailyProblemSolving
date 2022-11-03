#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<int> bags;
vector<pair<int, int>> jewels;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> k;

    // 보석 입력
    for (int i = 0; i < n; i++)
    {
        int m, v;
        cin >> m >> v;
        jewels.push_back({m, v});
    }
    // 가방
    for (int i = 0; i < k; i++)
    {
        int b;
        cin >> b;
        bags.push_back(b);
    }

    sort(jewels.begin(), jewels.end());
    sort(bags.begin(), bags.end());

    priority_queue<int> pq;
    long long ret = 0;
    int idx = 0;

    for (int i = 0; i < k; i++)
    {
        while (idx < n && jewels[idx].first <= bags[i])
        {
            pq.push(jewels[idx].second);
            idx++;
        }
        if (pq.size())
        {
            ret += pq.top();
            pq.pop();
        }
    }
    cout << ret << "\n";

    return 0;
}