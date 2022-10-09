#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[104][104];
int visited[104][104];
const int dx[] = {1, -1, 0, 0};
const int dy[] = {0, 0, 1, -1};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> n >> m;
    
    for(int i = 1; i < n + 1; i++){
        string s;
        cin >> s;
        for(int j = 0; j < m; j++)
            arr[i][j+1] = s[j] - '0';
    }

    queue<pair<int, int>> q;
    q.push({1, 1});
    visited[1][1] = 1;
    while(!q.empty()){
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(1 <= nx && nx < n + 1 && 1 <= ny && ny < m + 1){
                if(!visited[nx][ny] && arr[nx][ny] == 1){
                    visited[nx][ny] = visited[x][y] + 1;
                    q.push({nx, ny});
                }
            }
        }
    }
    cout << visited[n][m] << "\n";
    return 0;
}