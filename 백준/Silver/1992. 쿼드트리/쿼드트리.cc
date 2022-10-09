#include <bits/stdc++.h>
using namespace std;

int n;
int arr[65][65];
string s;
string dfs(int x, int y, int size){

    if(size == 1) return string(1, arr[x][y]);

    char current = arr[x][y];
    string ret = "";
    int h = size / 2;

    for(int i = x; i < x + size; i++){
        for(int j = y; j < y + size; j++){
            if(arr[i][j] != current) {
                ret += "(";
                ret += dfs(x, y, h);            // 순서 잘 맞춰야함
                ret += dfs(x, y + h, h);
                ret += dfs(x + h, y, h);
                ret += dfs(x + h, y + h, h);
                ret += ")";
                return ret;
            }
        }
    }   
    return string(1, arr[x][y]);
}

int main() {
    ios_base::sync_with_stdio(0); 
    cin.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> s;
        for(int j = 0 ; j < n; j++){
            arr[i][j] = s[j];
        }
    }

    cout << dfs(0, 0, n) << "\n";
    
    return 0;
}