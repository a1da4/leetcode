class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        N = len(grid[0])

        for row in grid:
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right) // 2 
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            answer += (N - left)

        return answer

