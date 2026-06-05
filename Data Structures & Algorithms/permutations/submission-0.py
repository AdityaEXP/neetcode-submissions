class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, subset):
            if i == n:
                res.append(subset.copy())
                return

            for num in nums:
                if num in subset:
                    continue

                subset.append(num)
                dfs(i+1, subset)
                subset.pop()


        dfs(0, [])

        return res