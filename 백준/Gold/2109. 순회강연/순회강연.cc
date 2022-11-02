#include <bits/stdc++.h>
using namespace std;

int n, ret;
vector<pair<int, int>> v;
priority_queue<int, vector<int>, greater<int>> pq;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int d, p;
        cin >> p >> d;
        v.push_back({d, p});
    }

    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++)
    {
        pq.push(v[i].second);
        if (pq.size() > v[i].first)
        {
            pq.pop();
        }
    }

    while (pq.size())
    {
        ret += pq.top();
        pq.pop();
    }

    cout << ret << "\n";

    return 0;
}