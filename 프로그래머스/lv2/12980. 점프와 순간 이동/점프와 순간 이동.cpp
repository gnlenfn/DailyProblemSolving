#include <iostream>
using namespace std;

int solution(int n)
{
    int ans = 0;
    
    while(n) {
        int tmp = n % 2;
        n /= 2;
        if(tmp) ans++;
    }

    return ans;
}