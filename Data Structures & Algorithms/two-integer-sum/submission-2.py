class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # method 2

        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                j = nums[i+1:].index(target-nums[i])+(i+1)
                return [i,j]