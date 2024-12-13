class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        N = len(nums)
        marked = [False] * N

        heap = []
        for numId, num in enumerate(nums):
            heapq.heappush(heap, (num, numId))
        
        while heap:
            num, numId = heapq.heappop(heap)
            if marked[numId]:
                continue
            marked[numId] = True
            if numId > 0:
                marked[numId - 1] = True
            if numId < N - 1:
                marked[numId + 1] = True
            
            score += num

        return score

