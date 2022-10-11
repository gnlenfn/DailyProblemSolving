#include <bits/stdc++.h>
using namespace std;

char grid[101][101];
int visited[101][101];
int h, w;
vector<pair<int, int>> v;
int main() {

    cin >> h >> w;
    for(int row = 0; row < h; row++){
        for(int col = 0; col < w; col++){
            scanf(" %c", &grid[row][col]);
            if(grid[row][col] == 'c') v.push_back({row, col});
        }
    }
    
    fill(&visited[0][0], &visited[0][0] + 101 * 101, -1);
    for(auto c : v){
        int x, y;
        queue<pair<int, int>> q;
        tie(x, y) = c;
        q.push({x, y});
        visited[x][y] = 0;

        while (!q.empty()){
            int r, c;
            tie(r, c) = q.front();
            q.pop();

            int nc = c + 1;
            if(nc < w){
                visited[r][nc] = visited[r][c] + 1;
                q.push({r, nc});
            }
        }
    }

    for(int row = 0; row < h; row++){
        for(int col = 0; col < w; col++){
            cout << visited[row][col] << " ";
        }
        cout << "\n";
    }
    
    return 0;
}