class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0    
        profit = 0
        buyDay = 0
        for currentDay in range(1, len(prices) - 1):
            if prices[currentDay - 1] >= prices[currentDay] < prices[currentDay + 1]:
                if buyDay is not None and prices[buyDay] < prices[currentDay]:
                    continue
                buyDay = currentDay
            
            elif prices[currentDay - 1] <= prices[currentDay] > prices[currentDay + 1]:
                if buyDay is None or prices[buyDay] > prices[currentDay]:
                    continue
                profit += prices[currentDay] - prices[buyDay]
                buyDay = None
        
        if buyDay is not None and prices[buyDay] < prices[-1]:
            profit += prices[-1] - prices[buyDay]
         
        return profit
