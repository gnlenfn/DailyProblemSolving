#include <bits/stdc++.h>

using namespace std;

int tmp[] = {0, 0};

void quad(int x, int y, int size, vector<vector<int>> &arr){
    int current = arr[x][y];
    int h = size / 2;
    bool flag = true;
    
    if(size == 1){
        tmp[current]++;
        return;
    }       
    
    for(int i = x; i < x + size; i++){
        for(int j = y; j < y + size; j++){
            if(arr[i][j] != current) {
                flag = false;
            }
        }
    }
    if(flag){
        tmp[current]++;
        return;
    } 
    else {
        quad(x, y, h, arr);
        quad(x, y + h, h, arr);
        quad(x + h, y, h, arr);
        quad(x + h, y+ h, h, arr);
    }
    
}

vector<int> solution(vector<vector<int>> arr) {
    vector<int> answer;
    
    quad(0, 0, arr.size(), arr);
    answer.push_back(tmp[0]);
    answer.push_back(tmp[1]);
    return answer;
}