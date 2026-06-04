class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        # Validating each row
        positions = {}
        for i in range (9):
            for j in range(9):
                value = board[i][j]
                # if value == ".": continue
                positions[str(i) + str(j)] = board[i][j]

        # validating each row
        for j in range(9):
            is_found = set()
            keys = [f"{i}{j}" for i in range(9)]
            for key in keys:
                value = positions[key]
                if value == ".": continue
                if value in is_found:
                    return False
                else:
                    is_found.add(value)

        # validating each column
        for j in range(9):
            is_found = set()
            keys = [f"{j}{i}" for i in range(9)]
            for key in keys:
                value = positions[key]
                if value == ".": continue
                if value in is_found:
                    return False
                else:
                    is_found.add(value)

        # Validating each 3x3 sub-grid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()

                for k in range(3):
                    for l in range(3):
                        value = board[i + k][j + l]
                        if value != '.':
                            if value in seen:
                                return False
                            seen.add(value)

        return True