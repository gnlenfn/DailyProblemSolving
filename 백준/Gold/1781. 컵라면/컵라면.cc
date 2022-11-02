#include <bits/stdc++.h>
using namespace std;

int n;
int ret;
priority_queue<int, vector<int>, greater<int>> pq;
vector<pair<int, int>> v;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int d;
        int c;

        cin >> d >> c;
        v.push_back({d, c});
    }

    sort(v.begin(), v.end());
    for (int i = 0; i < v.size(); i++)
    {
        ret += v[i].second;
        pq.push(v[i].second);
        if (pq.size() > v[i].first){
            ret -= pq.top();
            pq.pop();
        }
    }

    cout << ret << "\n";
    return 0;
}