class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        f(i, j) = can we make s3[i+j:] from s1[i:] and s2[j:]

        case1: s3[i+j:] matches from s1[i]
        case1: s3[i+j:] matches from s2[j]
        case3: matches from both
        """

        if len(s1) + len(s2) != len(s3):
            return False

        if not s1 and not s2 and not s3:
            return True

        memo = {}

        def f(i, j):
            
            if (i + j) == len(s3):
                return True

            if (i, j) in memo: return memo[(i, j)]

            ans = False 

            if i < len(s1) and s3[i + j] == s1[i]:
                ans = ans or f(i + 1, j)
            
            if j < len(s2) and s3[i + j] == s2[j]:
                ans = ans or f(i, j + 1)

            memo[(i, j)] = ans
            return ans 

        return f(0, 0)




            
            
