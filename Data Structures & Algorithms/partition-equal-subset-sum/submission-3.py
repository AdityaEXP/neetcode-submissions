class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if not S % 2 == 0:
            return False

        to_form = int(S / 2)

        memo = {}

        def dfs(i, currsum):
            if (i, currsum) in memo: return memo[(i, currsum)]

            if i == len(nums):
                return False

            if currsum == to_form:
                return True 

            if currsum > to_form:
                return False

            memo[(i, currsum)] = dfs(i+1, currsum + nums[i]) or dfs(i + 1, currsum)
            
            return memo[(i, currsum)]

        return dfs(0, 0)
