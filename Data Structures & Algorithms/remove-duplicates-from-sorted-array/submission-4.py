class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)

        while r < n:
            if nums[r] != nums[l]:
                l+=1
                nums[l] = nums[r]

            r+=1

        return l + 1

        