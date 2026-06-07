class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        """
        f(i) -> can first i word be created?
        f(0) -> True

        choices?
        - start from i and loop backward to j and check if substring j:i+1 is in wordDict, 
        if yes store it into memo and start dfs(j)
        """

        memo = {0: True}
        wordDict = set(wordDict)
        
        def f(i):
            if i in memo: return memo[i]

            memo[i] = any(
                f(j) and s[j:i] in wordDict 
                for j in range(0, i)
            )
            return memo[i]
            

        return f(n)            

