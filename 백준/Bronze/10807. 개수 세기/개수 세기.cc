#include <bits/stdc++.h>
using namespace std;

int n, arr[101], v;
int main() {
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    cin >> v;
    
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(arr[i] == v) cnt++;
    }
    
    cout << cnt << endl;
}