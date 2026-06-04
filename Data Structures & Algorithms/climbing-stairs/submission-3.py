class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1

        def memonization(n, cache):
            if n in [2, 3]:
                return n

            if n in cache:
                return cache[n]

            cache[n] = memonization(n-1, cache) + memonization(n-2, cache)
            return cache[n]

        return memonization(n, {})
        