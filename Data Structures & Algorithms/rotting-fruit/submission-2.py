class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen = set()
        q = deque()
        total_minutes = 0

        ROWS, COLUMNS = len(grid), len(grid[0])

        is_fresh_exists = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    is_fresh_exists = True

        if not q:
            if is_fresh_exists:
                return -1
            else:
                return 0

        while q:
            print("level", q)
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    R, C = r + dr, c + dc

                    if (R < 0 or C < 0) or (R >= ROWS or C >= COLUMNS) or ( (R, C) in seen ):
                        continue

                    if grid[R][C] == 1:
                        grid[R][C] = 2
                        q.append((R, C))
                    
                    seen.add((R, C))
            
            total_minutes+=1
            print("end", total_minutes)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return total_minutes - 1

        