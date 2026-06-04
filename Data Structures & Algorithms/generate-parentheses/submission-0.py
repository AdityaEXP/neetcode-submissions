class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(subset, open_count, close_count):
            if len(subset) == n*2:
                res.append("".join(subset))
                return

            if open_count < n:
                subset.append("(")
                backtrack(subset, open_count + 1, close_count)
                subset.pop()

            if open_count > close_count:
                subset.append(")")
                backtrack(subset, open_count, close_count + 1)
                subset.pop()
            

        backtrack([], 0, 0)
        return res