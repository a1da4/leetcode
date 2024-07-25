class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        
        answer = []
        while heap:
            answer.append(heapq.heappop(heap))
        
        return answer
