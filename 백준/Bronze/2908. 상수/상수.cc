#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int rev(string s) {

    reverse(s.begin(), s.end());
    return atoi(s.c_str());
}

int main() {
    string a, b;
    int answer;
    
    cin >> a >> b;

    answer = rev(a) < rev(b) ? rev(b) : rev(a);
    
    cout << answer << endl;
    
    return 0;
}