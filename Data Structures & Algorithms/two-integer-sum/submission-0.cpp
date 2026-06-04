#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> cmp;

        for (int i = 0; i < nums.size(); i ++) {
            int ele = nums[i];
            

            if (cmp.count(target - ele) == 1) {
                return {cmp[target - ele], i};
            }

            cmp[ele] = i;

        }
    }
};
