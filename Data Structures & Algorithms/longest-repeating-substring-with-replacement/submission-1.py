class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        window valid if (window size - most occuring character) <= k
        """

        n = len(s)

        l, r = 0, 0

        fmap = {}
        most_occ = 0

        max_size = 0

        while r < n:
            fmap[s[r]] = fmap.get(s[r], 0) + 1
            most_occ = max(most_occ, fmap[s[r]])

            while ( (r - l + 1) - most_occ ) > k:
                fmap[s[l]] -= 1

                if fmap[s[l]] == 0:
                    del fmap[s[l]]

                l+=1

            max_size = max(max_size, r - l + 1)
            r+=1

        return max_size