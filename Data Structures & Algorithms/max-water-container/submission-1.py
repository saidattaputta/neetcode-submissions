class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_cap = 0

        while left < right:
            min_h = min(heights[left],heights[right])
            width = right - left
            pro = min_h * width
            max_cap = max(max_cap,pro)
            while left<right and heights[left] == min_h:
                left += 1
            while left<right and heights[right] == min_h:
                right -= 1
        return max_cap