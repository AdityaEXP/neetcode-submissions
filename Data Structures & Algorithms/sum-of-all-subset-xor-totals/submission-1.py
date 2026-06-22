class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, currxor):
            if i ==  len(nums):
                return currxor
            
            total_sum = 0
            total_sum+=dfs(i + 1, currxor ^ nums[i])
            total_sum+=dfs(i + 1, currxor)
            return total_sum

        return dfs(0, 0)
