#include <bits/stdc++.h>
using namespace std;

string str, bomb, ret;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(NULL);

    cin >> str >> bomb;
    for(char c : str) {
        ret += c;
        if(ret.size() >= bomb.size() && ret.substr(ret.size() - bomb.size(), bomb.size()) == bomb) {
            ret.erase(ret.end() - bomb.size(), ret.end());
        }
    }

    if(!ret.size()) cout << "FRULA" << "\n";
    else cout << ret << "\n";

    return 0;
}