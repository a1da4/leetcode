class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        totalCost = float("inf")
        currTotalQuality = 0
        wage2quality = []

        for i in range(n):
            wage2quality.append((wage[i] / quality[i], quality[i]))

        wage2quality.sort(key=lambda x: x[0])
        workers = []

        for i in range(n):
            heapq.heappush(workers, -wage2quality[i][1])
            currTotalQuality += wage2quality[i][1]

            if len(workers) > k:
                currTotalQuality += heapq.heappop(workers)

            if len(workers) == k:
                totalCost = min(totalCost, currTotalQuality * wage2quality[i][0])

        return totalCost
