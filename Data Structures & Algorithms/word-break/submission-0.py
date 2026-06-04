class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True

        wordDict = set(wordDict)

        for i in range(1, n + 1):

            for j in range(i, -1, -1):
                if j < 0:
                    continue 

                if s[j-1:i] in wordDict and dp[j-1]:
                    dp[i] = True
                    break

        return dp[n]
    


            

