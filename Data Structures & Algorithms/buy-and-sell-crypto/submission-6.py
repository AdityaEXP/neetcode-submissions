class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 1:
            return 0

        l, r = 0, 1
        max_profit = 0

        while r < n:
            profit = prices[r] - prices[l]

            if profit > 0:
                max_profit = max(profit, max_profit)
            else:
                l = r

            r+=1

        return max_profit
