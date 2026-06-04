class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        max_length = 0

        for num in seen:
            # expand only if num is the start
            if (num - 1) not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                max_length = max(max_length, length)

        return max_length
        