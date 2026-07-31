class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        conslen = 0
        dummy = 0
        
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] == nums[i]+1:
                dummy += 1
                conslen = max(conslen,dummy)
            else:
                dummy = 0
        return conslen+1