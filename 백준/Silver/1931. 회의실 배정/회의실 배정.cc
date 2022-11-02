#include <bits/stdc++.h>
using namespace std;

int n, ret = 1;
vector<pair<int, int>> v;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int from, to;
        cin >> from >> to;
        v.push_back({to, from});
    }
    sort(v.begin(), v.end());

    int from = v[0].second;
    int to = v[0].first;

    for(int i = 1; i < n; i++){
        if(to > v[i].second) continue;

        from = v[i].second;
        to = v[i].first;
        ret++;
    }

    cout << ret << "\n";
    return 0;
}