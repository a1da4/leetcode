class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if n == 0:
            return 0
        INF = float("inf")

        # create cost matrix
        w = [[] for _ in range(n)]
        for flight in flights:
            fromId, toId, cost = flight
            w[fromId].append((toId, cost))

        # define dp matrix
        dp = [[INF] * n for _ in range(k + 2)]
        dp[0][src] = 0
        
        # each step
        answers = []
        for currStep in range(k + 1):
            heaps = [(cost, node) for node, cost in enumerate(dp[currStep])]
            heapq.heapify(heaps)
            while heaps:
                currCost, currNode = heapq.heappop(heaps)
                if currCost == INF:
                    break
                for (nextNode, nextCost) in w[currNode]:
                    dp[currStep + 1][nextNode] = min(dp[currStep + 1][nextNode],
                                                    currCost + nextCost)
            heapq.heappush(answers, dp[currStep + 1][dst])
        cost = heapq.heappop(answers)
        if cost == INF:
            return -1
        else:
            return cost
