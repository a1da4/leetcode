class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for numId, num in enumerate(nums):
            heapq.heappush(heap, (-num, numId))
        
        ansIds = []
        for _ in range(k):
            _, numId = heapq.heappop(heap)
            ansIds.append(numId)
        
        return [nums[ansId] for ansId in sorted(ansIds)]

