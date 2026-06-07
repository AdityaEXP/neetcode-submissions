class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]


        memo = {
            0: nums[0],
            1: max(nums[0], nums[1])
        }

        def robRecursion(i):
            if i in memo: return memo[i]

            ans = max(
                nums[i] + robRecursion(i-2),
                robRecursion(i-1)
            )
            memo[i] = ans 
            return ans

        return robRecursion(n-1)
        