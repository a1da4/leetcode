class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = []
        for num in nums:
            heapq.heappush(squares, num**2)
        answer = []
        while squares:
            answer.append(heapq.heappop(squares))
        
        return answer
