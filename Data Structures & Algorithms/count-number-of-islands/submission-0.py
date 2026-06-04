class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Thought process:
        - first time seeing this question and its my first graph question.
        - the knowledge i have is currently how to do dfs on graph to count number of ways to go from
        (0, 0) to (m, n), the recursive and backtracking solution!!.
        - according to the question an island is lands formed by connecting adjacent lands 
        horizontally and vertically, i.e we dont go diagonally.
        - Land = 1, Water = 0
        - and all the edges are water, i.e out bound is water as well.
        - my approach can be:
            1. iterate whole graph like matrix then when we find apply dfs.

            2. the dfs will keep looking for other 1 if the coordinate of 1 is unseen add it in island count.
        """

        island = 0

        seen = set()

        def dfs(grid, r, c, seen):
            ROWS, COLUMNS = len(grid), len(grid[0])

            if min(r, c) < 0:
                return
            
            if r == ROWS or c == COLUMNS:
                return

            if (r, c) in seen:
                return

            if grid[r][c] == "0":
                return

            seen.add((r, c))

            dfs(grid, r + 1, c, seen) # down
            dfs(grid, r - 1, c, seen) # up
            dfs(grid, r , c + 1, seen) # right
            dfs(grid, r , c - 1, seen) # left

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # print(r, c)
                if grid[r][c] == "1":
                    if not (r, c) in seen:
                        island+=1

                    dfs(grid, r, c, seen)

        return island


