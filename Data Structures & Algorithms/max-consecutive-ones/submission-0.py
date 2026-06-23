class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max_val = 0

        for ch in nums:
            if ch == 0:
                max_val = max(max_val, curr)
                curr = 0
            else:
                curr+=1

        max_val = max(max_val, curr)

        return max_val