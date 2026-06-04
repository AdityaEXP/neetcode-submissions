class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        seen_index = None

        for i, ele in enumerate(nums):
            to_find = target - ele
            if to_find in seen:
                return [seen[to_find], i]

            seen[ele] = i

        return 0, 0
            

        