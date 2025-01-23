class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row2num = [0] * m
        col2num = [0] * n
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    row2num[row] += 1
                    col2num[col] += 1

        answer = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    if row2num[row] > 1 or col2num[col] > 1:
                        answer += 1

        return answer

