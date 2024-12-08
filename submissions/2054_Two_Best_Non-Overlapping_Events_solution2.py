class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        maxVal, maxSum = 0, 0
        for start, end, val in events:
            while heap and heap[0][0] < start:
                maxVal = max(maxVal, heap[0][1])
                heapq.heappop(heap)
            maxSum = max(maxSum, val + maxVal)
            heapq.heappush(heap, (end, val))

        return maxSum

