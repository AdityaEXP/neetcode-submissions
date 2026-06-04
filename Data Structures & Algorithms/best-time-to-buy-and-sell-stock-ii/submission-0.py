class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0

        profit = 0

        l, r = 0, 1
        while r < n:
            p = prices[r] - prices[l]

            if p > 0:
                profit+=p
                l=r
            else:
                l=r
            
            r+=1

        return profit