#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[100001];
int visited[100001];
int cnt; // 방법의 수
int ans; // 최단거리
int cur, num;

int bfs(int a, int t){
    queue<pair<int, int>> q;
    q.push({a, t});  // 현재 위치와 현재 위치까지 이동 시간 push

    while(!q.empty()){
        int x, y; // x : 현재위치 y : 이동 시간
        tie(x, y) = q.front();
        q.pop();
        visited[x] = 1;

        if(x == m){ // 동생을 찾음
            if(cnt == 0){
                ans = y;
                cnt++;
            } 
            else if(cnt > 0 && ans == y) cnt++;
        }

        int go[3] = {x + 1, x - 1, x * 2};
        for(int i = 0; i < 3; i++){
            int na = go[i];

            if(na < 0 || na > 100000) continue;
            if(visited[na]) continue;

            q.push({na, y + 1});
        }
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n >> m;

    bfs(n, 0);
    cout << ans << "\n" << cnt << "\n";
    return 0;
}