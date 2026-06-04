class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l, r = 0, 0

        maxFreq = dict()
        max_length = 0
        while r < n:

            

            maxFreq[s[r]] = maxFreq.get(s[r], 0) + 1
            while ((r - l + 1) - max(maxFreq.values())) > k:
                maxFreq[s[l]]-=1
                l+=1
            max_length = max(max_length, r - l + 1)

            r += 1

        return max_length
