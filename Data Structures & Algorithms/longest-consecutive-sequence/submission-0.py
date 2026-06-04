class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set()
        may_start = set()
        for num in nums:
            if not num in seen:
                seen.add(num)
            
            if (num - 1) in seen:
                may_start.add(num - 1)

        max_length = 0

        for num in nums:
            start = num
            a = 1
            length = 1

            while True:
                if (start + a) in seen:
                    a += 1
                    length += 1
                else:
                    break
            max_length = max(max_length, length)

        return max_length

        