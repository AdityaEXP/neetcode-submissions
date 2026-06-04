class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        1. how do we even know if we robbed first house as its dynamic

        """

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        def getMax(nums):
            n = len(nums)

            dp = [0] * n 
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(
                    nums[i] + dp[i-2],
                    dp[i-1]
                )

            return dp[n-1]
        
        ans = [
            getMax(nums[1:]),
            getMax(nums[: len(nums)-1])
        ]

        print(ans)
        return max(
            ans
        )

