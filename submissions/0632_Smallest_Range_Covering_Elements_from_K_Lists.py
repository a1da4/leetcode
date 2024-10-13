class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        maxVal = -float("inf")
        N = len(nums)
        ns = [len(nums[i]) for i in range(N)]
        for i in range(N):
            heapq.heappush(pq, (nums[i][0], i, 0))
            maxVal = max(maxVal, nums[i][0])

        rStart, rEnd = 0, float("inf")
        while len(pq) == N:
            minVal, row, col = heapq.heappop(pq)
            if maxVal - minVal < rEnd - rStart:
                rStart, rEnd = minVal, maxVal
            if col + 1 < ns[row]:
                nextVal = nums[row][col + 1]
                heapq.heappush(pq, (nextVal, row, col + 1))
                maxVal = max(maxVal, nextVal)

        return [rStart, rEnd]

