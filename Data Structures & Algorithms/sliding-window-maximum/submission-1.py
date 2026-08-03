class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxlist = []
        window = []
        left = 0
        have = 0
        for right in range(len(nums)):
            window.append(nums[right])
            have +=1
            if have == k:
                maxi = max(window)
                maxlist.append(maxi)
                have -= 1
                window.remove(nums[left])
                left += 1
        return maxlist