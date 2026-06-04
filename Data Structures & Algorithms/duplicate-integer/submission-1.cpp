#include <set>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> mp;

        for(int i = 0; i < nums.size(); i++){
            int element = nums[i];

            if (mp.find(element) != mp.end()){
                return true;
            } else {
                mp.insert(element);
            };
        };

        return false;
    };
};