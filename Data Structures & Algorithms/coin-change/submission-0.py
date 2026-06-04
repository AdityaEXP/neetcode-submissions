class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = min number of coin required to form i

        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                temp = i - c
                if temp >= 0:
                    dp[i] = min(dp[i], 1 + dp[temp])

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
