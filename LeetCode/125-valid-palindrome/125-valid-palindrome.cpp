class Solution {
public:
    bool isPalindrome(string s) {
        string conc = "";
        for(auto &c : s){
            if(isalnum(c)) conc += tolower(c);
        }

        string tmp = conc;
        reverse(tmp.begin(), tmp.end());
        
        if(tmp == conc) return true;
        else return false;
    }
};