class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        same as LCS two pointers on word 1 and word 2.
        i and j

        main goal should be explore all possible combo. later think about greedy if exists

        so base case should be afcourse when word1 == word2

        or when string becomes empty?

        hmm noo

        f(i, j) -> min number of operations required to convert
        word1[i:] into word2[j:]

        base cases? 
        both i and j exhausted -> success

        i exhausted but j left that means we need to insert j - i word 

        i left but j exhausted means we need to delete i - j word
        """

        memo = {}

        m1, m2 = len(word1), len(word2)

        def f(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if i >= m1 and j >= m2:
                return 0 # word matched 
            
            if i >= m1 and j < m2:
                return m2 - j # j - i insertion left 
            
            if j >= m2 and i < m1:
                return m1 - i # i - j deletetion left

            operations = float("inf")

            if word1[i] == word2[j]:
                operations = min(operations, f(i+1, j+1))
            
            # if not matches then try to replace
            operations = min(
                operations,
                1 + f(i + 1, j + 1)
            )

            # also try deleting
            operations = min(
                operations,
                1 + f(i + 1, j)
            )

            # try inserting
            operations = min(
                operations,
                1 + f(i, j + 1)
            )

            memo[(i,j)] = operations

            return operations

        return f(0, 0)
