class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {
            0: cost[0],
            1: cost[1],
        }

        n = len(cost)
        for i in range(2, n):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])

        return min(memo[n-1], memo[n-2])