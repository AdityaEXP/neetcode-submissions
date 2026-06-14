class Solution:
    def jump(self, nums: List[int]) -> int:

        current_end = 0
        jumps = 0
        next_reach = 0

        for i in range(len(nums)-1):
            next_reach = max(next_reach, i + nums[i])
            
            if i == current_end:
                jumps+=1
                current_end = next_reach


        return jumps

            

        