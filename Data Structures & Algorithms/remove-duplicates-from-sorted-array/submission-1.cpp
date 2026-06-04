class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = 1;
        int r = 1;

        int n = nums.size();

        while(r < n){
            if(nums[r] != nums[r-1]){
                nums[l] = nums[r];
                l+=1;
            }
            r+=1;
        }

        return l;
    }
};