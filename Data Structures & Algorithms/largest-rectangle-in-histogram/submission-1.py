class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = heights + [0,]
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                current_height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, width * current_height)
            stack.append(i)
            
        return max_area











            



        


