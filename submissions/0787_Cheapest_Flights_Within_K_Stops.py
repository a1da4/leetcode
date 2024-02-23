class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if n == 0:
            return 0
        INF = float("inf")

        # create cost matrix
        w = [[INF] * n for _ in range(n)]
        for flight in flights:
            fromId, toId, cost = flight
            w[fromId][toId] = min(w[fromId][toId], cost)        

        # define dp matrix
        dp = [[INF] * n for _ in range(k + 2)]
        dp[0][src] = 0
        
        # each step
        for currStep in range(k + 1):
            for currNode in range(n):
                if dp[currStep][currNode] == INF:
                    continue
                nextNodes = [nextNode for nextNode in range(n)
                                if w[currNode][nextNode] != INF]
                for nextNode in nextNodes:
                    dp[currStep + 1][nextNode] = min(dp[currStep + 1][nextNode],
                                                    dp[currStep][currNode] + w[currNode][nextNode])
        cost = min([dp[step][dst] for step in range(k + 2)])
        if cost == INF:
            return -1
        else:
            return cost
