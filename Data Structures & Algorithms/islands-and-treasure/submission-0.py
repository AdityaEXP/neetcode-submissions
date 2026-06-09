class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque()

        ROWS, COLUMNS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLUMNS):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        directions = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]
        length = 0

        while q:

            for _ in range(len(q)):
                r, c = q.popleft()

                if grid[r][c] == 2147483647:
                    grid[r][c] = length

                for dr, dc in directions:
                    R, C = r + dr, c + dc
                    if ( min(R, C) < 0 or
                        R >= ROWS or C >= COLUMNS or
                        (R, C) in visited or 
                        grid[R][C] == -1

                    ):
                        continue
                    
                    q.append((R, C))
                    visited.add((R, C))

            length+=1

                