#include <bits/stdc++.h>
using namespace std;

int n, ans = INT_MIN;
string str;
vector<int> num;
vector<char> ops;
int calc(int a, int b, char op)
{
    if (op == '+')
        return a + b;
    else if (op == '-')
        return a - b;
    else if (op == '*')
        return a * b;
    return 0;
}

void go(int idx, int ret)
{
    if (idx == ops.size())
    {
        ans = max(ans, ret);
        return;
    }
    go(idx + 1, calc(ret, num[idx + 1], ops[idx]));

    if (idx + 2 <= ops.size())
    {
        int tmp = calc(num[idx + 1], num[idx + 2], ops[idx + 1]);
        go(idx + 2, calc(ret, tmp, ops[idx]));
    }
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> str;
    for (char s : str)
    {
        if (isdigit(s))
            num.push_back(s - '0');
        else
            ops.push_back(s);
    }
    go(0, num[0]);
    cout << ans << "\n";
    return 0;
}