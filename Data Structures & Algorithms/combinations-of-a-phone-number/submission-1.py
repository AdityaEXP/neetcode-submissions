class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        n = len(digits)

        if digits == "": return []

        combo = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        } 

        def backtrack(i, res):

            if len(res) == n:
                answer.append("".join(res))
                return

            current_int = int(digits[i])

            for alph in combo[current_int]:
                res.append(alph)
                backtrack(i + 1, res)
                res.pop()

        backtrack(0, [])

        return answer
        
            


            
        