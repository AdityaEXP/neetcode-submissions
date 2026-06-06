class Solution:
    def build_board(self, subset, n):
        board = ["." * n for _ in range(n)]

        for r, c in subset:
            row = ["."] * n
            row[c] = "Q"
            board[r] = "".join(row)

        return board

    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        ROWS, COLUMNS = n, n

        def dfs(row, cols, dia1, dia2, subset):
            # base case
            if row == ROWS:
                res.append(self.build_board(subset.copy(), n))
                return

            for col in range(COLUMNS):

                if (
                    col in cols or 
                    row - col in dia1 or
                    row + col in dia2
                ):
                    continue 

                subset.append((row, col))
                cols.add(col)
                dia1.add(row - col)
                dia2.add(row + col)
                dfs(row+1, cols, dia1, dia2, subset)

                subset.pop()
                cols.remove(col)
                dia1.remove(row - col)
                dia2.remove(row + col)
            



        dfs(0, set(), set(), set(), [])
        # need to preprocess res before returning
        return res
