class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0

        seen = set()

        def dfs(grid, r, c, seen):
            ROWS, COLUMNS = len(grid), len(grid[0])

            if min(r, c) < 0:
                return 0
            
            if r == ROWS or c == COLUMNS:
                return 0

            if (r, c) in seen:
                return 0

            if grid[r][c] == 0:
                return 0

            seen.add((r, c))

            count = 1

            count += dfs(grid, r + 1, c, seen) # down
            count += dfs(grid, r - 1, c, seen) # up
            count += dfs(grid, r , c + 1, seen) # right
            count += dfs(grid, r , c - 1, seen) # left

            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (not (r,c) in seen):
                    area = dfs(grid, r, c, seen)
                    max_area = max(area, max_area)

        return max_area

