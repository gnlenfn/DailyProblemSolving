#include <bits/stdc++.h>
using namespace std;

int n, ans;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        string w;
        set<char> s;
        cin >> w;

        bool flag = false;
        s.insert(w[0]);
        for (int i = 1; i < w.size(); i++)
        {
            if (w[i] == w[i - 1])
                continue;
            if (s.find(w[i]) != s.end())
            {
                flag = true;
                break;
            }
            s.insert(w[i]);
        }
        if (!flag)
            ans++;
    }

    cout << ans << "\n";
    return 0;
}