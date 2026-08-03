class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxpro = 0
        left = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                maxpro = max(maxpro,prices[right]-prices[left])
        return maxpro