class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buyPrice0 = buyPrice1 = float("inf")
        sellPrice0 = sellPrice1 = 0
        for price in prices:
            buyPrice0 = min(buyPrice0, price)
            sellPrice0 = max(sellPrice0, price - buyPrice0)
            buyPrice1 = min(buyPrice1, price - sellPrice0)
            sellPrice1 = max(sellPrice1, price - buyPrice1)
        return sellPrice1
