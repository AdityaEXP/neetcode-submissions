class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tf, seen = {}, {}
        for x in t:
            tf[x] = tf.get(x, 0) + 1

        n = len(s)
        l = r = 0
        
        required = len(tf.keys())
        formed = 0

        answer = "x" * 2000
        while r < n:
            
            #seen[s[r]] = seen.get(s[r], 0) + 1
            if s[r] in tf:
                seen[s[r]] = seen.get(s[r], 0) + 1
            
                if seen[s[r]] == tf[s[r]]:
                    formed+=1

            

            while formed == required:
                size = r - l + 1
                if size < len(answer):
                    answer = s[l: r+1]

                if s[l] in tf:
                    if seen[s[l]] == tf[s[l]]:
                        formed -= 1
            
                    seen[s[l]]-=1
                    if seen[s[l]] == 0:
                        del seen[s[l]]
                l+=1


            r+=1

        return "" if answer == "x"*2000 else answer

