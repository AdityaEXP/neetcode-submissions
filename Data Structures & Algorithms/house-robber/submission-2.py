class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max amount of money we can get till ith house
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = {
            0: nums[0],
        }

        dp[1] = max(nums[1], nums[0])

        for i in range(2, n):
            dp[i] = max(
                nums[i] + dp[i-2], # rob current
                dp[i-1] # skip current
            )

        return dp[n - 1]

