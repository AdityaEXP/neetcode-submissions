class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        q = deque()
        seen = set()

        seen.add((0, 0))
        q.append((0, 0))

        length = 1
        found_length = False

        if grid[0][0] == 1:
            return -1
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLUMNS - 1:
                    found_length = True
                    return length

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                directions = directions + [[1, 1], [-1, -1], [1, -1], [-1, 1]]

                for dr, dc in directions:
                    R, C = r + dr, c + dc
                    if ( (R < 0 or C < 0) or ( R >= ROWS or C >= COLUMNS) or (grid[R][C] == 1) or ((R, C) in seen)):
                        continue

                    q.append((R, C))
                    seen.add((R, C))

            length +=1

        return length if found_length else -1

