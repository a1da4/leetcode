class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        numPrice = len(prices)
        rowHold = [0] * numPrice
        rowFree = [0] * numPrice
        
        rowHold[0] = -prices[0]

        for i in range(1, numPrice):
            rowHold[i] = max(rowHold[i - 1], rowFree[i - 1] - prices[i])
            rowFree[i] = max(rowFree[i - 1], rowHold[i - 1] + prices[i] - fee) 

        return rowFree[-1]
