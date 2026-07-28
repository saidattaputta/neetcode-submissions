class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        
        for i in range(len(nums)):
            curr_prod = 1
            for j in range(len(nums)):
                if i != j:
                    curr_prod *= nums[j]
            output.append(curr_prod)
        return output