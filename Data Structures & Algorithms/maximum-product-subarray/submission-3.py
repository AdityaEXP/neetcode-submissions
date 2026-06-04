class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]

        n = len(nums)

        dpMin = [1] * n
        dpMax = [1] * n

        dpMin[0], dpMax[0] = nums[0], nums[0]

        for i in range(1, n):
            min_ans = nums[i] * dpMin[i-1]
            max_ans = nums[i] * dpMax[i-1]

            ans = max(
                nums[i],
                min_ans,
                max_ans,
                ans
            )


            dpMin[i] = min(min_ans, nums[i], max_ans)
            dpMax[i] = max(max_ans, nums[i], min_ans)

        return ans

