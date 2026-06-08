class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}

        def f(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if i == m or j == n: return 0
            if i == m - 1 or j == n - 1: return 1

            memo[(i, j)] = f(i+1, j) + f(i, j + 1)
            return memo[(i, j)]

        return f(0, 0)
