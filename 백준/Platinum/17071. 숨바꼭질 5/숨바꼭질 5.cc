#include <bits/stdc++.h>
using namespace std;

int n, k, turn = 1;
int visited[2][500001];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> k;
    if (n == k)
    {
        cout << 0 << "\n";
        return 0;
    }

    queue<int> q;
    q.push(n);
    visited[0][n] = 1; // 짝수 번째에 도착과 홀수 번째에 도착하는 것을 구분 (turn % 2)

    bool flag = false;
    while (q.size())
    {
        k += turn;
        if (k > 500000)
            break; // 발견 불가
        if (visited[turn % 2][k])
        { // 동생발견
            flag = 1;
            break;
        }

        int qs = q.size();
        for (int i = 0; i < qs; i++)
        { // turn이 있기 때문에 이번 턴에 큐에 넣은 것들만 방문 --> 그다음은 턴 증가
            int x = q.front();
            q.pop();
            for (int nx : {x + 1, x - 1, 2 * x})
            {
                if (nx < 0 || nx > 500000 || visited[turn % 2][nx])
                    continue;
                
                visited[turn % 2][nx] = 1;
                if (nx == k)
                {
                    flag = 1;
                    break;
                }
                q.push(nx);
            }
            if (flag)
                break;
        }
        if (flag)
        {
            flag = 1;
            break;
        }
        turn++;
    }
    if (flag)
        cout << turn << "\n";
    else
        cout << -1 << "\n";
    return 0;
}