class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if n == k:
            return 0

        minHeap = []
        maxHeap = []
        for i in range(n - 1):
            pairSum = weights[i] + weights[i + 1]
            heapq.heappush(minHeap, pairSum)
            heapq.heappush(maxHeap, -pairSum)

        minScore = 0
        maxScore = 0
        for _ in range(k - 1):
            minPairSum = heapq.heappop(minHeap)
            _maxPairSum = heapq.heappop(maxHeap)
            maxPairSum = -1 * _maxPairSum

            minScore += minPairSum
            maxScore += maxPairSum
        
        return maxScore - minScore

