class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left = 1
        right = max(piles)
        ans = h

        while left <= right:
            speed = (left+right)//2
            
            hours = sum((pile + speed - 1) // speed for pile in piles)

            if hours <= h:
                ans = speed
                right = speed - 1
            else:
                left = speed + 1
        return ans