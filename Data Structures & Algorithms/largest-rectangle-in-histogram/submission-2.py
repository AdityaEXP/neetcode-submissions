class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        area = min_height_from_range(l, r)
        """

        stack = []
        n = len(heights) + 1
        heights.append(-1)
        max_area = 0

        for i in range(n):

            while stack and heights[i] < heights[stack[-1]]:
                right_index = i
                height_min = heights[stack.pop()]
                left_index = stack[-1] if stack else -1
                max_area = max(
                    max_area,
                    (right_index - left_index - 1) * height_min
                )

            stack.append(i)

        return max_area