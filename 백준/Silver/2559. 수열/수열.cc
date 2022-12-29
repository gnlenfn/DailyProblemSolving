#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    int n, k;
    vector<int> v;

    cin >> n >> k;

    int sum = 0;
    v.push_back(sum);
    for(int i = 0; i < n; i++){
        int tmp;
        cin >> tmp;
        sum += tmp;
        v.push_back(sum);
    }

    vector<int> max;
    for(int i = k; i < n + 1; i++){
        max.push_back(v[i] - v[i - k]);
    }
    cout << *max_element(max.begin(), max.end()) << "\n";
    return 0;
}