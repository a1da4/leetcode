class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = []
        for rowId in range(1, len(grid)-1):
            currRow = []
            for colId in range(1, len(grid)-1):
                currRow.append(
                    max(grid[rowId-1][colId-1:colId+2] + \
                        grid[rowId][colId-1:colId+2] + \
                        grid[rowId+1][colId-1:colId+2])
                )
            answer.append(currRow)
        return answer
