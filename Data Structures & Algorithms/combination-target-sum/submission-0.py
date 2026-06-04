class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        n = len(nums)

        def backtrack(res, total_sum, i = 0):
            if total_sum == target:
                answer.append(res.copy())
                return
            

            if total_sum > target:
                return

            for i in range(i, n):
                num = nums[i]
                res.append(num)
                backtrack(res, total_sum + num, i)
                res.pop()

        backtrack([], 0)

        return answer
