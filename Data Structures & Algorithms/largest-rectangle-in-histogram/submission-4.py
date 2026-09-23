class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices
        res = 0

        for i, h in enumerate(heights + [0]):  
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left_smaller_index = stack[-1] if stack else -1
                width = i - left_smaller_index - 1
                res = max(res, height * width)
            stack.append(i)

        return res