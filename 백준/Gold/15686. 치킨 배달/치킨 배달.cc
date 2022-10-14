#include <bits/stdc++.h>
using namespace std;

int n, m, city[51][51];
vector<pair<int, int>> _home, chicken;
vector<vector<int>> chickenList;

// 어디 치킨집을 살릴 지 선택하는 함수 (조합)
void combi(int start, vector<int> v)
{
    if (v.size() == m)
    {
        chickenList.push_back(v);
        return;
    }
    for (int i = start + 1; i < chicken.size(); i++)
    {
        v.push_back(i);
        combi(i, v);
        v.pop_back();
    }
    return;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> n >> m;

    int result = INT_MAX;
    int current = 0;
    // 지도 그리기 및 집 좌표, 치킨집 좌표 확인
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> city[i][j];
            if (city[i][j] == 1)
                _home.push_back({i, j});
            if (city[i][j] == 2)
                chicken.push_back({i, j});
        }
    }

    // m개만 남기고 모두 폐업시킬 것
    vector<int> v; // 치킨집 선택 경우의 수
    combi(-1, v);  // 각각 경우의 수(v)를 chickenList로 push

    for (vector<int> cList : chickenList) // 모든 경우의 수 탐색
    {
        int ret = 0;
        for (pair<int, int> home : _home)
        {
            int _min = INT_MAX;
            for (int ch : cList)
            {
                // 집 1개와 살아남은 치킨집 사이의 맨하탄거리를 구한 뒤 최소값을 ret에 저장
                int _dist = abs(home.first - chicken[ch].first) + abs(home.second - chicken[ch].second);
                _min = min(_min, _dist);
            }
            ret += _min;
        }
        result = min(result, ret);
    }

    cout << result << "\n";

    return 0;
}