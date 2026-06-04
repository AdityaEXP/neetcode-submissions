class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        l, r = 0, 0

        while r < n:
            if nums[r] == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1

            r+=1
        
        l, r = n - 1, n - 1

        while r > 0:
            if nums[r] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                l-=1
            
            r-=1

        return nums
        