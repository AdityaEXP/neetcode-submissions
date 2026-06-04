class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = 1
        ss = s[0]

        for i in range(len(s)):

            # for odd length
            l, r = i, i

            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    ss = s[l:r+1]

                l-=1
                r+=1

            # for even length
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest:
                    longest = r - l + 1
                    ss = s[l:r+1]
        
                l-=1
                r+=1

        return ss