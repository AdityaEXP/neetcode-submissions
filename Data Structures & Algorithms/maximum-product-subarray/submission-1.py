class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float("-inf")

        n = len(nums)

        for i in range(n):
            product = 1
            for j in range(i, n):
                product*=nums[j]
                ans = max(ans, product)

        return ans