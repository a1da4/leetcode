class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        x = heapq.heappop(heap)
        answer = 0
        while x < k:
            y = heapq.heappop(heap)
            heapq.heappush(heap, x * 2 + y)
            x = heapq.heappop(heap)
            answer += 1
        
        return answer 

