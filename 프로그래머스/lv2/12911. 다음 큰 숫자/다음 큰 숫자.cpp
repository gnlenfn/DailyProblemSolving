#include <bits/stdc++.h>

using namespace std;
int solution(int n) {
    int cnt = bitset<20>(n).count();
    
    while(bitset<20>(++n).count() != cnt);
    return n;
}