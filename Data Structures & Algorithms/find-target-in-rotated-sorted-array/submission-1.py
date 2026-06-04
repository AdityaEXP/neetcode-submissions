class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        def binarySearch(low, high, target):
            l, r = low, high

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    return mid

            return -1

        while l < r:
            mid = ( l + r ) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        break_point = l

        if nums[break_point] <= target <= nums[n - 1]:
            index = binarySearch(break_point, n - 1, target)
        else:
            index = binarySearch(0, break_point, target)

        return index
        
        # while l <= r:
        #     mid = (l + r) // 2

        #     if nums[left] <= nums[mid]: 
        #         # left side is sorted
        #         if nums[left] <= target <= nums[mid]:
        #             index = binarySearch(left, mid, target)
        #             return index
        #         else:


        #     if nums[left] >= nums[mid]:

