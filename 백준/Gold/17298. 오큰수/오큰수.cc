#include <bits/stdc++.h>
using namespace std;

int n;
stack<int> stk;
int a[1000001], ret[1000001];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    memset(ret, -1, sizeof(ret));
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        while (stk.size() && a[stk.top()] < a[i])
        {
            ret[stk.top()] = a[i];
            stk.pop();
        }
        stk.push(i);
    }

    for (int i = 0; i < n; i++)
    {
        cout << ret[i] << " ";
    }
    return 0;
}