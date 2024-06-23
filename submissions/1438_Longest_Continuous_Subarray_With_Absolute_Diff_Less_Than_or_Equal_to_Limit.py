class Solution:
    def longestSubarray(self, nums, limit):
        maxHeap = []
        minHeap = []

        left = 0
        maxLen = 0

        for right in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[right], right))
            heapq.heappush(minHeap, (nums[right], right))

            while -maxHeap[0][0] - minHeap[0][0] > limit:
                left = min(maxHeap[0][1], minHeap[0][1]) + 1
                while maxHeap[0][1] < left:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < left:
                    heapq.heappop(minHeap)

            maxLen = max(maxLen, right - left + 1)

        return maxLen
