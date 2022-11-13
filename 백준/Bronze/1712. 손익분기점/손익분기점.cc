#include <bits/stdc++.h>
using namespace std;

int a, b, c;
int main(){
    cin >> a >> b >> c;
    
    int per = c - b;
    if(per <= 0) {
        cout << -1;
        return 0;
    }
    int n = a / per;
    cout << n + 1;
    
    return 0;
}