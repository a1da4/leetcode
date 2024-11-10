class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, sell = -prices[0], 0
        for i in range(1, n):
            tmp = hold
            hold = max(hold, sell - prices[i])
            sell = max(sell, tmp + prices[i] - fee)
        
        return sell

