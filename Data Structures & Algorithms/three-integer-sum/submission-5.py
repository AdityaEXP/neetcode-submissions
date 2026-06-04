class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        
        for i in range(n):
            target = -nums[i]
            seen = set()

            for j in range(i+1, n):
                dt = target - nums[j]

                if dt in seen:
                    a = tuple(sorted([nums[i], nums[j], dt]))
                    if a not in res:
                        res.add(a)
                else:
                   seen.add(nums[j])
                
        return list(res)