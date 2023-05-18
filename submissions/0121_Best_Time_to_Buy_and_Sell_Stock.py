class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        minPrice = None
        for currentDay in range(len(prices)):
            if minPrice == None or prices[currentDay] < minPrice:
                minPrice = prices[currentDay]
            elif prices[currentDay] - minPrice > profit:
                profit = prices[currentDay] - minPrice

        return profit
