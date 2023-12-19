class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # initialize buys, sells into [float("inf")] * k+1, [0] * k+1
        buys = [float("inf")] * (k + 1)
        sells = [0] * (k + 1)

        for price in prices:
            for currId in range(1, k + 1):
                buys[currId] = min(buys[currId], price - sells[currId - 1])
                sells[currId] = max(sells[currId], price - buys[currId])

        return sells[-1]
