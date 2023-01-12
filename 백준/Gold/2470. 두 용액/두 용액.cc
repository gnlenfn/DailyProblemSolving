#include <bits/stdc++.h>
using namespace std;

int n, l, r;
vector<long long> v;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        long long tmp;
        cin >> tmp;
        v.push_back(tmp);
    }

    sort(v.begin(), v.end());
    long long cur = LONG_MAX;
    r = n - 1;

    pair<long long, long long> p;
    while (l < r)
    {
        if (abs(v[l] + v[r]) < cur)
        {
            cur = abs(v[l] + v[r]);
            p = {v[l], v[r]};
        }
        if (v[l] + v[r] < 0)
            l++;
        else if (v[l] + v[r] > 0)
            r--;
        else
        {
            cout << v[l] << " " << v[r];
            return 0;
        }
    }

    cout << p.first << " " << p.second;
    return 0;
}