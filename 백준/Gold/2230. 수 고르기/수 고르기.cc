#include <bits/stdc++.h>
using namespace std;

int n, m;
int a[100005];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    sort(a, a + n);
    int R = 1, ans = INT_MAX;
    for (int L = 0; L < n; L++)
    {
        while (a[R] - a[L] < m && R < n)
        {
            R++;
        }
        if (a[R] - a[L] >= m)
        {
            ans = min(ans, a[R] - a[L]);
        }
    }

    cout << ans << "\n";
    return 0;
}