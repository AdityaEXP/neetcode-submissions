class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLUMNS = len(heights), len(heights[0])

        p, a = set(), set()

        def pdfs(grid, r, c, limit, p):
            if (min(r, c) < 0 or
                r == ROWS or c == COLUMNS or
                grid[r][c] < limit or
                (r, c) in p
                ):
                return

            p.add((r,c))

            pdfs(grid, r+1, c,grid[r][c], p)
            pdfs(grid, r-1, c,grid[r][c], p)
            pdfs(grid, r, c+1,grid[r][c], p)
            pdfs(grid, r, c-1,grid[r][c], p)


        pacific_set = [(0, x) for x in range(COLUMNS)] + [(x, 0) for x in range(1, ROWS)]

        
        for r, c in pacific_set:
            if (r, c) not in p:
                pdfs(heights, r, c, heights[r][c], p)

        atlantic_set = [(ROWS-1, x) for x in range(COLUMNS)] + [(x, COLUMNS - 1) for x in range(ROWS-1)]

        for r, c in atlantic_set:
            if (r, c) not in a:
                pdfs(heights, r, c, heights[r][c], a)

        return list(p & a)
        

