#include <bits/stdc++.h>
using namespace std;

int r, c, cnt;
int arr[1505][1505];
int path_check[1505][1505];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
pair<int, int> start;
queue<pair<int, int>> swan, water, tmpS, tmpW;
bool found = false;
// 매번 visited를 초기화하면 시간초과가 뜨기 때문에 이번에 물로 변한 곳만 체크해본다.
// tmp 큐는 다음날 순회해볼 곳들
// swan, water는 오늘 순회할 곳들
void swanMeet()
{
    while (!swan.empty())
    {
        int x, y;
        tie(x, y) = swan.front();
        swan.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || ny < 0 || nx >= r || ny >= c || path_check[nx][ny])
                continue;
            path_check[nx][ny] = 1;

            if (arr[nx][ny] == 'X') // 빙하를 만나면 다음날 순회할 예정
                tmpS.push({nx, ny});
            else if (arr[nx][ny] == '.') // 물이면 다음 이동해야하므로 swan으로 푸쉬
                swan.push({nx, ny});
            else if (arr[nx][ny] == 'L')
            {
                found = true;
                break;
            }
        }
    }
}

void melt()
{
    while (!water.empty())
    {
        int x, y;
        tie(x, y) = water.front();
        water.pop();

        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx < 0 || nx >= r || ny < 0 || ny >= c)
                continue;

            if (arr[nx][ny] == 'X') // 방하를 만나면 물로 바꾼뒤 다음날 큐로 push
            {
                arr[nx][ny] = '.';
                tmpW.push({nx, ny});
            }
        }
    }
}

int checkDays()
{
    while (!found)
    {
        swanMeet();
        if (found)
        {
            return cnt;
        }
        melt();

        swan = tmpS;
        water = tmpW; // tmp큐가 기존까지 중복방문없이 방문할 곳들
        while (tmpS.size())
            tmpS.pop();
        while (tmpW.size())
            tmpW.pop();
        cnt++;
    }
    return cnt;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> r >> c;
    for (int i = 0; i < r; i++)
    {
        string s;
        cin >> s;
        for (int j = 0; j < s.size(); j++)
        {
            arr[i][j] = s[j];
            if (s[j] == 'L')
            {
                start.first = i;
                start.second = j; // 백조 둘 중 아무거나에서 출발하면 됨
            }

            if (s[j] != 'X')
                water.push({i, j}); // 백조있는 칸도 물
        }
    }

    path_check[start.first][start.second] = 1;
    swan.push(start);
    cout << checkDays() << "\n";

    return 0;
}