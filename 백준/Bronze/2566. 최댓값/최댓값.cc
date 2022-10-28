#include <bits/stdc++.h>
using namespace std;

int mat[9][9];
int maxVal = INT_MIN;
int main(){
    int row = 0, col = 0;
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            cin >> mat[i][j];
        }
    }
    
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            if(maxVal < mat[i][j]){
                maxVal = mat[i][j];
                row = i;
                col = j;
            }
        }
    }
    cout << maxVal << endl;
    cout << row + 1 << " " << col + 1;
}