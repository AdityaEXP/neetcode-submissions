class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []
        max_area = 0

        heights = heights + [0,]
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                h = heights[stack.pop()]
                right = i 

                try:
                    left = stack[-1]
                except:
                    left = - 1

                width = right - left - 1
                max_area = max(max_area, width * h)
            
            stack.append(i)
        
        return max_area

            













            



        


