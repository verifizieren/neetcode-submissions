class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(1, len(prices)): # Exclude first one
            if prices[r] < prices[l]: 
                l=r
            else:
                maxProfit = max(maxProfit, prices[r] - prices[l])
        return maxProfit