#include <bits/stdc++.h>

using namespace std;

int num = 0;
int recursion(const char *s, int l, int r){
    num++;
    if(l >= r) return 1;
    else if(s[l] != s[r]) return 0;
    else{
        return recursion(s, l+1, r-1);
    } 
}

int isPalindrome(const char *s){
    return recursion(s, 0, strlen(s)-1);
}

int main(){
    int t;
    cin >> t;

    for(int i = 0; i < t; i++) {
        char word[1001];
        cin >> word;

        cout << isPalindrome(word) << " " << num << "\n";
        num = 0;
    }
}