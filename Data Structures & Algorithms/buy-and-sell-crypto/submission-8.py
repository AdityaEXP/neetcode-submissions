class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        n = len(prices)

        l, r = 0, 1

        while r < n:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)

            if profit < 0:
                l = r

            r+=1
        

            
        return max_profit