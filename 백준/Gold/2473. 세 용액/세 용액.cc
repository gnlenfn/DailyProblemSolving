#include <bits/stdc++.h>
using namespace std;

int n;
vector<long long> arr;
long long int ans[3];

void input()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        long long tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    input();

    sort(arr.begin(), arr.end());
    long long best = LONG_MAX;

    for (int i = 0; i < n - 2; i++)
    {
        int left = i + 1, right = n - 1;

        while (left < right)
        {
            long long sum = arr[i] + arr[left] + arr[right];
            if (abs(best) > abs(sum))
            {
                best = sum;
                ans[0] = arr[i];
                ans[1] = arr[left];
                ans[2] = arr[right];
            }

            if (sum > 0)
                right--;
            else if (sum < 0)
                left++;
            else
            {
                i = n;
                break;
            }
        }
    }

    sort(ans, ans + 3);
    for (auto num : ans)
    {
        cout << num << " ";
    }
    return 0;
}