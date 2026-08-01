class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #  optimal

        n = numbers
        left,right = 0,len(n)-1
        while left < right:
            total = n[left] + n[right]
            if total == target:
                return [left+1,right+1]
            elif total < target:
                left += 1
            elif total > target:
                right -= 1
        