class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.stair2cost = {0: cost[0], 1: cost[1]}
        numStairs = len(cost)

        def findNextStair(stair: int) -> int:
            if stair not in self.stair2cost:
                self.stair2cost[stair] = cost[stair] + min(findNextStair(stair-1), findNextStair(stair-2))
            return self.stair2cost[stair]
        
        return min(findNextStair(numStairs-1), findNextStair(numStairs-2))
