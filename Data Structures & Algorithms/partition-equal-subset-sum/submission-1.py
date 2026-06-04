class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tsum = sum(nums)
        n = len(nums)

        if tsum % 2 != 0:
            return False

        to_find_sum = tsum // 2

        # if i can make to_find_sum with the help of nums then rest of the array auto equal!

        # can i do greedy? take max then slow down, dont think so 

        # how do i fit dp here?

        # do i do backtracking to build subset and the sum(subset) == to_find_sum is the answer?
        # the complexity will go 2^n with it. i can use memoization to lower down the complexity.
 
        cache = {}

        def dfs(i, curr_sum):
            # base case 0: memoization
            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]
            
            # base case 1: i > array
            if i >= n:
                return False

            # base case 2: sum > to_find_sum
            if curr_sum > to_find_sum:
                return False
            
            # base case 3: if sum == curr_sum
            if curr_sum == to_find_sum:
                return True

            ans = (
                dfs(i+1, curr_sum + nums[i])
                or
                dfs(i+1, curr_sum)
            )

            cache[(i, curr_sum)] = ans
                        
            return ans

        return dfs(0, 0)
