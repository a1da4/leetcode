class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        answer = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            row = i
            col = 0
            heap = []
            while row < n:
                heapq.heappush(heap, -grid[row][col])
                row += 1
                col += 1
            
            row = i
            col = 0
            while heap:
                answer[row][col] -= heapq.heappop(heap)
                row += 1
                col += 1
        
        for i in range(1, n):
            row = 0
            col = i
            heap = []
            while col < n:
                heapq.heappush(heap, grid[row][col])
                row += 1
                col += 1
            
            row = 0 
            col = i
            while heap:
                answer[row][col] += heapq.heappop(heap)
                row += 1
                col += 1

        return answer
