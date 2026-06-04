class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = dict()
        to_find = dict()

        for x in s1:
            to_find[x] = to_find.get(x, 0) + 1

        l, r = 0, 0
        n2 = len(s2)
        n1 = len(s1)


        while r < n2:
            seen[s2[r]] = seen.get(s2[r], 0) + 1
            size = r - l + 1
            if size > n1:
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                l += 1
            if to_find == seen:
                return True
            r+=1

        return False