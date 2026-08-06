class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        heights.append(0)
        maxarea = 0
        stack = []
        n = len(heights)

        for i,h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i
                maxarea = max(maxarea, (width*height))
            stack.append(i)
        return maxarea