class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = nums[0]

        left = 0
        right = n-1
        while left<=right:

            if nums[left]<=nums[right]:
                ans = min(ans,nums[left])
                break

            mid = (left+right)//2
            if nums[left] <= nums[mid]:
                ans = min(ans,nums[left])
                left = mid+1
            else:
                ans = min(ans,nums[mid])
                right = mid - 1
        return ans