#include <bits/stdc++.h>

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() < 3) return {};
        
        sort(nums.begin(), nums.end());
        if(nums[0] > 0) return {};
        
        vector<vector<int>> v;       
        for(int i = 0; i < nums.size() - 2; i++){
            int left = i + 1, right = nums.size() - 1;
            
            if(i > 0 && nums[i] == nums[i-1]) continue;
            
            while(left < right) {
                if(nums[i] + nums[left] + nums[right] == 0) {
                    v.push_back({nums[i], nums[left], nums[right]});
                    
                    while(left < right && nums[left] == nums[left + 1]) left++;
                    while(left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                }
                else if (nums[i] + nums[left] + nums[right] < 0) left++;
                else right--;
            }
        }
        
        return v;
    }
};