#include <bits/stdc++.h>
using namespace std;

int n, node, d, cnt, start;
vector<int> v[50];

int countLeaf(int k)
{
    int ret = 0, child = 0;
    for (auto there : v[k]) 
    {
        if(there == d) continue;
        ret += countLeaf(there);
        child++;
    }
    if(!child) return 1;
    return ret;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> n;
    // 인접리스트로 트리 구현
    for (int i = 0; i < n; i++)
    {
        cin >> node;
        if (node == -1) // root node
            start = i;

        else
            v[node].push_back(i);
    }

    cin >> d;    
    if(start == d) cout << 0 << "\n";
    else cout << countLeaf(start) << "\n";
    return 0;
}