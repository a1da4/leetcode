class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for numId, num in enumerate(nums):
            heapq.heappush(heap, (num, numId))
        
        for _ in range(k):
            num, numId = heapq.heappop(heap)
            nums[numId] *= multiplier
            heapq.heappush(heap, (num * multiplier, numId))

        return nums

