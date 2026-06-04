class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            total_time = 0

            for pile in piles:
                time = pile / mid
                if time > int(time):
                    time = int(time) + 1
                total_time += time

            if total_time <= h:
                right = mid

            if total_time > h:
                left = mid + 1

        return left
