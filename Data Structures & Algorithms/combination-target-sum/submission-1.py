class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        n = len(nums)

        def backtrack(res, i = 0):
            total_sum = sum(res)
            if total_sum == target:
                answer.append(res.copy())
                return
            

            if total_sum > target:
                return

            for i in range(i, n):
                num = nums[i]
                res.append(num)
                backtrack(res, i)
                res.pop()

        backtrack([], 0)

        return answer
