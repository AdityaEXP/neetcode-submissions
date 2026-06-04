class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = []
        n1, n2 = len(word1), len(word2)
        for i in range(max(n1, n2)):
            if n1 > i:
                s.append(word1[i])
            if n2 > i:
                s.append(word2[i])

        return "".join(s)

        