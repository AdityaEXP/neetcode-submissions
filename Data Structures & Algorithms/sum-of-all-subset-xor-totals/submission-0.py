class Solution:
    def generateXORSum(self, subset):
        temp = 0
        for ch in subset:
            temp ^= ch 

        return temp 

    def subsetXORSum(self, nums: List[int]) -> int:
        res = []

        def dfs(i, subset):
            if i ==  len(nums):
                res.append(subset[::])
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            #     i+=1
            dfs(i + 1, subset)

        dfs(0, [])
        return sum(self.generateXORSum(x) for x in res)
