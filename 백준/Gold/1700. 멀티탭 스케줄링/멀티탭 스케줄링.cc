#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<int> order;
int visited[101];
int solv()
{
    vector<int> plug;
    int target = INT_MAX, ans = 0;

    for (int i = 0; i < order.size(); i++)
    {
        int elec = order[i];

        // 사용중이라면?
        if (visited[elec])
            continue;

        // 콘센트 자리 있으면?
        if (plug.size() < n)
        {
            plug.push_back(elec);
            visited[elec] = 1;
            continue;
        }

        // 가장 늦게 사용할 기기 제거
        int lastIdx = 0;
        for (int x = 0; x < plug.size(); x++)
        {
            int future = INT_MAX;
            for (int y = i + 1; y < order.size(); y++) // 순서상 다음 기기부터 인덱스 확인
            {
                if (order[y] == plug[x]) // 이후 순서에 플러그에 있는 기기 사용됨
                {
                    future = y; // 이후 몇번째에 사용하는지 기록
                    break;
                }
            }
            if (future > lastIdx) // future 이번에 확인하는 기기 다음에 나올 인덱스
            {
                // t가 INT_MAX면 이후에 안쓴다는 뜻
                // target은 플러그에서 뽑을 기기 인덱스
                lastIdx = future;
                target = x;
            }
        }

        // 교체
        int targetNum = plug[target];
        visited[targetNum] = 0;
        plug[target] = elec;
        visited[elec] = 1;

        ans++;
    }

    return ans;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> k;
    for (int i = 0; i < k; i++)
    {
        int tmp;
        cin >> tmp;
        order.push_back(tmp);
    }

    cout << solv() << "\n";
    return 0;
}