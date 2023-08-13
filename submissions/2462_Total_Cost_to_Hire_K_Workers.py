class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        headCosts = costs[:candidates]
        tailCosts = costs[max(candidates, len(costs)-candidates):]
        heapq.heapify(headCosts)
        heapq.heapify(tailCosts)

        headNext = candidates
        tailNext = len(costs) - candidates - 1
        totalCost = 0
        for i in range(k):
            if not tailCosts or headCosts and headCosts[0] <= tailCosts[0]:
                totalCost += heapq.heappop(headCosts)
                if headNext <= tailNext:
                    heapq.heappush(headCosts, costs[headNext])
                    headNext += 1
            else:
                totalCost += heapq.heappop(tailCosts)
                if tailNext >= headNext:
                    heapq.heappush(tailCosts, costs[tailNext])
                    tailNext -= 1
            
        return totalCost
