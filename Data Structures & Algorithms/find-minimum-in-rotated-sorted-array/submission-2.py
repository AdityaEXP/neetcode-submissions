class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        minimum_element = float('inf')

        minimum_element = nums[0]
        while r < n:
            mid = (l+r) // 2

            if nums[mid] > nums[mid - 1]:
                l = mid
            else:
                minimum_element = min(nums[mid], minimum_element)
                break
            r-=1


        return minimum_element
