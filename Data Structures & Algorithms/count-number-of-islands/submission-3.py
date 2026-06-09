class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        approch iterate grid and run dfs on every 1 i find and in dfs i wil change every 1 to 0 to marked them as explored!
        """
        totalIsland = 0
        ROWS, COLUMNS = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                min(r, c) < 0 or 
                r >= ROWS or
                c >= COLUMNS or
                grid[r][c] != "1"
            ):
                return 

            grid[r][c] = "0"

            directions = [ [1,0], [-1, 0], [0, 1], [0, -1] ]
            for dr, dc in directions:
                dfs(
                    r + dr, c + dc,
                )

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == "1":
                    totalIsland+=1
                    dfs(i, j)

        return totalIsland
        



