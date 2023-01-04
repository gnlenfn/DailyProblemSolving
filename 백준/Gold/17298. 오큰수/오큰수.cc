#include <bits/stdc++.h>
using namespace std;

int n;
int nums[1000005], ret[1000005];
stack<int> stk;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    memset(ret, -1, sizeof(ret));
    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
        while (stk.size() && nums[stk.top()] < nums[i])
        {
            ret[stk.top()] = nums[i];
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