class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, column = len(matrix), len(matrix[0])
        n = rows * column - 1

        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2

            ri, c = divmod(mid, column)

            value = matrix[ri][c]

            if value == target:
                return True

            if value > target:
                r = mid - 1
            
            if value < target:
                l = mid + 1

        return False