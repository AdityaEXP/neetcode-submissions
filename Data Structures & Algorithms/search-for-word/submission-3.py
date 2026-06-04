class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        okay wrote a code but its not correct

        now thinking, a word has been given so for each recursion path we need to track the words it has in
        and that word Counter should match the wordmap variable.

        for that we iterate grid and whenever we find a word which is in the wordmap we start dfs,
        and dfs track visit here is temp.
        
        base conditions?
        if row or column go out of bound.
        length of seen > len word
        the board[r][c] is not in word which is given.

        cmap == wordmap found it update answer = true

        then from a valid word we start dfs and go all four direction following base case.
        
        """

        ROWS, COLUMNS = len(board), len(board[0])

        def dfs(i, r, c, seen):
            
            if( min(r, c) < 0 or
                r >= ROWS or c >= COLUMNS or
                board[r][c] != word[i] or
                (r, c) in seen
            ):
                return False

            seen.add((r, c))

            if i == len(word) - 1:
                return True
            
            directions = [ [1,0], [-1,0], [0,1], [0,-1] ]

            for dr, dc in directions:
                R, C = r + dr, c + dc

                if dfs(i+1, R, C, seen):
                    return True

            seen.remove((r,c))

            return False


        for i in range(ROWS):
            for j in range(COLUMNS):
                w = board[i][j]

                if w == word[0]:
                    if dfs(0, i, j, set()):
                        return True

        return False

        
        