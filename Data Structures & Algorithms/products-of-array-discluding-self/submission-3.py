class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        right_map, right_product = {}, 1

        for i in range(n-1, -1, -1):
            right_map[i] = right_product
            right_product*=nums[i]

        left_map, left_product = {}, 1

        for i in range(n):
            left_map[i] = left_product
            left_product*=nums[i]

        answer = []

        for i in range(n):
            answer.append(
                left_map[i] * right_map[i]
            )

        return answer
            