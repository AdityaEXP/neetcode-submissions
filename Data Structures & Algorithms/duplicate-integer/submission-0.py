class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        is_duplicate = False
        all_values = set()
        for x in nums:
            if x in all_values:
                is_duplicate =  True
            else:
                all_values.add(x)
        
        return is_duplicate
         