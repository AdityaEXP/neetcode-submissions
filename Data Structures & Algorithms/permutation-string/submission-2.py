class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        window_size = len(s1)

        if window_size > n:
            return False

        l, r = 0, 0
        fmap = {}

        to_compare = {}

        while r < window_size:
            to_compare[s1[r]] = to_compare.get(s1[r], 0) + 1
            fmap[s2[r]] = fmap.get(s2[r], 0) + 1
            r+=1

        while r < n:
            if fmap == to_compare:
                return True 

            fmap[s2[l]] = fmap.get(s2[l], 0) - 1
            if fmap[s2[l]] == 0: del fmap[s2[l]]

            l+=1

            fmap[s2[r]] = fmap.get(s2[r], 0) + 1
            r+=1

        if to_compare == fmap: return True
            

        return False

        