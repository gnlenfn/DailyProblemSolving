#include <bits/stdc++.h>
using namespace std;

int n, mp, mf, ms, mv;
int p, f, s, v, sum, ret = INT_MAX;
map<int, vector<vector<int>>> tab;
struct A
{
    int mp, mf, ms, mv, cost;
} a[16];

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    cin >> mp >> mf >> ms >> mv;
    for (int i = 0; i < n; i++)
    {
        // 구조체 형태로 재료별 영양소 입력
        cin >> a[i].mp >> a[i].mf >> a[i].ms >> a[i].mv >> a[i].cost;
    }

    for (int i = 1; i < (1 << n); i++)
    {
        p = f = s = v = sum = 0;
        vector<int> vec;
        for (int j = 0; j < n; j++)
        {
            if (i & (1 << j))
            {
                // 4가지 영양소 이므로 총 2^4 경우의수
                // j 번째 비트 켜져있나 확인하며 해당 경우의수 영양소 함량 확인
                vec.push_back(j + 1);
                p += a[j].mp;
                f += a[j].mf;
                s += a[j].ms;
                v += a[j].mv;
                sum += a[j].cost;
            }
        }
        // 4개 영양소 기준 넘는지 확인, 비용이 기존 최소값보다 작거나 같으면 새로 push
        if (p >= mp && f >= mf && s >= ms && v >= mv && ret >= sum)
        {
            ret = sum;
            tab[ret].push_back(vec);
        }
    }

    if (ret == INT_MAX)
        cout << -1 << "\n";
    else
    {
        // 사전순 정렬
        sort(tab[ret].begin(), tab[ret].end());
        cout << ret << "\n";

        // 식재료 정렬
        sort(tab[ret][0].begin(), tab[ret][0].end());
        for (int e : tab[ret][0])
        {
            cout << e << " ";
        }
    }

    return 0;
}