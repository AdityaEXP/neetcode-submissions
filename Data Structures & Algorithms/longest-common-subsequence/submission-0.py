class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        memo = {}

        m1, m2 = len(text1), len(text2)

        def dfs(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if i >= m1 or j >= m2:
                return 0
            
            if text1[i] == text2[j]:
                ans = 1 + dfs(i + 1, j + 1)
            else:
                ans = max(
                    dfs(i + 1, j),
                    dfs(i, j + 1)
                )

            memo[(i, j)] = ans 
            return ans

        return dfs(0, 0)