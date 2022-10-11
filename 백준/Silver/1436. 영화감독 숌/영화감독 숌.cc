#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int target, cnt = 0;
    cin >> target;
    for(int i = 666;;i++){
        int tmp = i;
        while(tmp >= 666){
            if(tmp % 1000 == 666){
                cnt++;
                break;
            }
            tmp /= 10;
        }
        if(cnt == target){
            cout << i << "\n";
            break;
        }
    }

    
    return 0;
}