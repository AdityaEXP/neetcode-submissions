class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            target = -nums[i]
            while left < right:
                total_sum = nums[i] + nums[right] + nums[left]
                if total_sum == 0:
                    res.append([nums[i], nums[right], nums[left]])
                    left+=1
                    right-=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                elif total_sum > 0:
                        right-=1
                else:
                    left+=1
        return res