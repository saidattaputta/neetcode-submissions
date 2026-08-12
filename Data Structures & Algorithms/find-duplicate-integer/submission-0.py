class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = seen.get(num,0)+1
            else:
                return num
                break