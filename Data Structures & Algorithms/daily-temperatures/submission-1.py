class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                oldI, oldT = stack[-1]
                answer[oldI] = index - oldI
                stack.pop()

            stack.append((index, temp))

        return answer