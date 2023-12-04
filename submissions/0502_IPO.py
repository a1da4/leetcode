class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        sortedPairs = sorted([(cap, pro) for cap, pro in zip(capital, profits)])
        numPairs = len(sortedPairs)
        candidates = []
        i = 0
        for _ in range(k):
            while i < numPairs and w >= sortedPairs[i][0]:
                heapq.heappush(candidates, -sortedPairs[i][1])
                i += 1
            if not candidates:
                break
            w -= heapq.heappop(candidates)
        return w
