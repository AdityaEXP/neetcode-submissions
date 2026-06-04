class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen, n = set(), len(s)
        l, r = 0, 0

        max_length = 0
        while r < n:
            while s[r] in seen and r < n:
                seen.remove(s[l])
                l+=1

            max_length = max(max_length, r - l + 1)
            seen.add(s[r])
            r+=1

        return max_length
        