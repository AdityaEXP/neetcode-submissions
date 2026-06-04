class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]

        n = len(nums)

        prevMin = 1
        prevMax = 1

        prevMin, prevMax = nums[0], nums[0]

        for i in range(1, n):
            min_ans = nums[i] * prevMin
            max_ans = nums[i] * prevMax

            ans = max(
                nums[i],
                min_ans,
                max_ans,
                ans
            )


            prevMin = min(min_ans, nums[i], max_ans)
            prevMax = max(max_ans, nums[i], min_ans)

        return ans

