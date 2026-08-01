class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_cap = 0

        while left < right :
            min_h = min(heights[left],heights[right])
            width = right - left
            max_cap = max(width * (min_h),max_cap)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_cap