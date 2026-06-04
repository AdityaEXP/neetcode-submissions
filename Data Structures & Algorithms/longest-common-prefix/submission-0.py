class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""

        min_len = float("inf")
        min_word = ""
        for x in strs:
            if len(x) < min_len:
                min_len = len(x)
                min_word = x
        
        for i in range(min_len):
            temp = min_word[i]

            for s in strs:
                if not s[i] == temp:
                    return longest_prefix
            
            longest_prefix+=temp
        
        return longest_prefix

        