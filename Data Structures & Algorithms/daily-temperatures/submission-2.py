class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0] * n  
        
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                _, index = stack.pop()
                result[index] = i - index

            stack.append((temperatures[i], i))

        return result