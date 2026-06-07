class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # state  dp[i] = min number of coin required to form i
        # choices? 
        """
        to create i, we try all coins from coin list
        so choice is min (
            1 + dp[i - coin] for coin in coins 
        )

        and its recuroins as well
        """

        memo = {0: 0}
        def minCoin(amount):
            if amount in memo:
                return memo[amount]

            if amount in coins:
                memo[amount] = 1
                return 1
            
            if amount < 0:
                return float("inf")
            
            temp = float("inf")
            for c in coins:
                diff = amount - c
                temp = min(temp, 1 + minCoin(diff))
            memo[amount] = temp
            return temp 

        ans = minCoin(amount)
        return -1 if ans == float("inf") else ans