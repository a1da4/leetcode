class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, keep, reset = -float('inf'), -float('inf'), 0
        for price in prices:
            prevSell = sell
            sell = keep + price
            keep = max(keep, reset - price)
            reset = max(reset, prevSell)

        return max(sell, reset)

