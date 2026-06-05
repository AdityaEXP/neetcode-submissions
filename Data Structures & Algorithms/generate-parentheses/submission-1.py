class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(subset, open_used, close_used):
            # base case
            if len(subset) == n*2:
                res.append("".join(subset))
                return

            if close_used > open_used:
                return

            # backtrack logic
            if open_used < n:
                subset.append("(")
                dfs(subset, open_used+1, close_used)
                subset.pop()

            if close_used < n:
                subset.append(")")
                dfs(subset, open_used, close_used+1)
                subset.pop()

        dfs([], 0, 0)
        return res