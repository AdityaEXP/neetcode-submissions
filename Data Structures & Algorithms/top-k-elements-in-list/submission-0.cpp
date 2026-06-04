#include <vector>
#include <unordered_map>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        unordered_map<int, int> grps;

        for (auto i: nums) {
            grps[i]++;
        }

        vector<vector<int>> buckets(nums.size() + 1);

        for(const auto&pair: grps) {
            int number = pair.first;
            int frequency = pair.second;

            buckets[frequency].push_back(number);
        }

        vector<int> result;

        for(int i = buckets.size() - 1; i >=0 & result.size() < k; --i) {

            if (!buckets[i].empty()) {
                for (auto ele: buckets[i]) { result.push_back(ele); }
            }

        }

        return result;
    }
};
