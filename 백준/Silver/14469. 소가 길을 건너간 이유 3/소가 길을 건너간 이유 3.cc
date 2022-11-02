#include <bits/stdc++.h>
using namespace std;

int n, from, to, a, b, ret;
vector<pair<int, int>> v;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a >> b;
        from = a;
        to = b;

        v.push_back({from, to});
    }

    sort(v.begin(), v.end());
    ret = v[0].first + v[0].second;
    for (int i = 1; i < v.size(); i++){
        ret = max(ret, v[i].first);
        ret += v[i].second;
    }


    cout << ret << "\n";
    return 0;
}