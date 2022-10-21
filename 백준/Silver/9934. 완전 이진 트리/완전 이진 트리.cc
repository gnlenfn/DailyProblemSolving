#include <bits/stdc++.h>
using namespace std;

int k;
int arr[1050];
vector<int> v[10];
void divArr(int l, int r, int d){
    if(d >= k) return; // depth, 트리 높이 최대치

    if(l == r){  // 리프 노드
        v[d].push_back(arr[l]);
        return;
    }

    int m = (l + r) / 2;
    v[d].push_back(arr[m]);
    divArr(l, m - 1, d + 1);
    divArr(m + 1, r, d + 1);
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> k;
    int n = pow(2, k) - 1;

    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    divArr(0, n-1, 0);

    for(int i = 0; i < k; i++){
        for(auto num : v[i]) cout << num << " ";
        cout << "\n";
    }
    
    return 0;
}