#include <bits/stdc++.h>
using namespace std;

int r, c;
char maze[1001][1001];
int fire_check[1001][1001];
int hoon_check[1001][1001];
int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> r >> c;
    // 불은 못가지만 지훈이는 가는 경우가 있을 수 있음 
    // 지훈이 이동 시 불의 시간보다 작은 곳을 가라 했으므로 불 방문 체크는 가장 큰수로 초기화
    fill(&fire_check[0][0], &fire_check[0][0] + 1001 * 1001, INT_MAX); 

    pair<int, int> hoon;
    pair<int, int> fire;
    queue<pair<int, int>> fq;
    queue<pair<int, int>> hq;

    for(int i = 0; i < r; i++){
        string tmp;
        cin >> tmp;
        for(int j = 0; j < c; j++){
            maze[i][j] = tmp[j];
            if(maze[i][j] == 'J') hq.push({i, j});
            if(maze[i][j] == 'F'){
                // 불의 시작점이 하나가 아닐 수 있다
                fq.push({i, j});
                fire_check[i][j] = 1;
            } 

        }
    }  

    // - bfs 불 먼저 ㄱㄱ
    // - 지훈 이동 시 같은 시간의 불 못넘도록
    
    // 1. 불 이동
    while(!fq.empty()){
        int x, y;
        tie(x, y) = fq.front();
        fq.pop();

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || ny < 0 || nx >= r || ny >= c) continue;
            if(fire_check[nx][ny] != INT_MAX || maze[nx][ny] == '#') continue;
            if(fire_check[nx][ny] < fire_check[x][y] + 1) continue;

            fire_check[nx][ny] = fire_check[x][y] + 1;
            fq.push({nx, ny});
        }
    }

    // 2. 지훈 이동
    // fire_check에는 불이 해당 칸에 도착한 시간이 있음
    // 지훈이는 이동하면서 현재 시간이 해당 칸의 불의 시간보다 작아야 함
    // 가장자리에 도착하면 break
    hoon_check[hq.front().first][hq.front().second] = 1;
    while(!hq.empty()){
        int x, y;
        tie(x, y) = hq.front();
        hq.pop();

        if(x == 0 || y == 0 || x == r - 1 || y == c - 1) {
            cout << hoon_check[x][y] << "\n";
            return 0;
        }

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx < 0 || ny < 0 || nx >= r || ny >= c) continue;      // 미로 범위 check
            if(hoon_check[nx][ny] || maze[nx][ny] == '#') continue;   // 벽 check
            if(fire_check[nx][ny] <= hoon_check[x][y] + 1) continue;  // 불 check

            hoon_check[nx][ny] = hoon_check[x][y] + 1;
            hq.push({nx, ny});
        }
    }

    cout << "IMPOSSIBLE" << "\n";
    return 0;
}