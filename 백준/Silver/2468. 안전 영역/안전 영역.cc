#include <bits/stdc++.h>
using namespace std;

int n, ret=1;
int arr[101][101];
const int dx[] = {1, -1, 0, 0};
const int dy[] = {0, 0, 1, -1};
void dfs(int x, int y, int h, int visited[101][101]){

    for(int i = 0; i < 4; i++){
        int nx = x + dx[i];
        int ny = y + dy[i];

        if(0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && arr[nx][ny] > h){
            visited[nx][ny] = 1;
            dfs(nx, ny, h, visited);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            cin >> arr[i][j];
        }
    }


    for(int h = 1; h < 101; h++){
        int visited[101][101] = {0,};
        int tmp = 0;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(!visited[i][j] && arr[i][j] > h){                    
                    dfs(i, j, h, visited);
                    tmp++;
                }
            }
        }
        if(!tmp) break;
        ret = max(ret, tmp);
    }
    
    cout << ret << "\n";
    return 0;
}