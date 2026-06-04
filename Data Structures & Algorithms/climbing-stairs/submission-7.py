class Solution:
    def climbStairs(self, n: int) -> int:
        
        def solve(n, memo={1: 1, 2: 2}):
            if n in memo:
                return memo[n]

            ans = solve(n-1) + solve(n-2)
            memo[n] = ans
            return ans

        return solve(n)