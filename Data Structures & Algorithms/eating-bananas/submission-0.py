class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canFinish(piles, speed, h):
            total_time = 0
            for pile in piles:
                time = (pile + speed - 1) // speed
                total_time += time

            return total_time <=h
        
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            if canFinish(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
