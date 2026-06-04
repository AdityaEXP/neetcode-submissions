class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def check(k):
            total_time = 0

            for p in piles:
                total_time+= math.ceil(p / k)

            return total_time <= h

        while l < r:
            mid = (l + r) // 2

            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l