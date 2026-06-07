class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0

        n = len(s)

        """
        state: f(i) -> number of ways i decode with first i character!
        choice: f(i) -> read i as 1 single number if between 1 and 9, or read i and i+1 as single.
        recurence: f(i) = f(i-1) (if number bw 1 and 9) + f(i-2) (number is bw 10 and 26)
        """

        memo = {0: 1}
        def f(i):
            if i in memo: return memo[i]

            ways = 0
            if 1 <= int(s[i-1]) <= 9:
                ways+= f(i-1)
            print(i)
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                ways += f(i-2)

            memo[i] = ways
            return ways

        return f(n)

            
            

        



