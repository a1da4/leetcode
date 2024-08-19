class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        minCost = 0
        for house in range(1, n):
            for currColor in range(k):
                best = float("inf")
                for prevColor in range(k):
                    if currColor == prevColor:
                        continue
                    best = min(best, costs[house - 1][prevColor])
                costs[house][currColor] += best

        return min(costs[-1])

