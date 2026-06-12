class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, currsum):
            if (i, currsum) in memo: return memo[(i, currsum)]

            if i == len(nums):
                if currsum == target:
                    return 1
                else:
                    return 0

            ways = 0
            ways += dfs(i + 1, currsum + nums[i])
            ways += dfs(i + 1, currsum - nums[i])
            memo[(i, currsum)] = ways 
            return ways 

        return dfs(0, 0)