class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # optimal
        maxpro = 0
        left = 0
        for right in range(1,len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                pro = prices[right] - prices[left]
                maxpro = max(maxpro,pro)
        return maxpro