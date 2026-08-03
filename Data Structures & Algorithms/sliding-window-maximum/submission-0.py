class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxlist = []
        window = []
        have = 0
        left = 0
        for right in range(left,len(nums)):
            window.append(nums[right])
            have += 1
            if have == k:
                maxy = max(window)
                maxlist.append(maxy)
                have -=1
                window.remove(nums[left])
                left +=1
        return maxlist
            