class Solution:
    def minWindow(self, s: str, t: str) -> str:
        to_find = {}

        for x in t:
            to_find[x] = to_find.get(x, 0) + 1

        seen = {}
        n = len(s)

        l, r = 0, 0
        required = len(to_find.keys())
        formed = 0

        answer = "x" * 2000

        while r < n:
            

            if s[r] in to_find:
                seen[s[r]] = seen.get(s[r], 0) + 1
                if seen[s[r]] == to_find[s[r]]:
                    formed+=1

            while formed == required:
                size = r - l + 1
                if size < len(answer):
                    answer = s[l: r+1]

                if s[l] in to_find:
                    if seen[s[l]] == to_find[s[l]]:
                        formed-=1
    
                    seen[s[l]]-=1      
                    if seen[s[l]] <= 0:
                        del seen[s[l]]   
                    
                l+=1

            r+=1

        return answer if answer != "x" * 2000 else ""
