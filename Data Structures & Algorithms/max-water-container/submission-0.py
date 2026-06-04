class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        
        for i in range(n):
            for j in range(i+1, n):
                area = min(heights[i], heights[j]) * abs(i - j)
                max_area = max(area, max_area)

        return max_area
