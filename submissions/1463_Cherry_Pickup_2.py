class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        numCol = len(grid[0])
        prevDp = defaultdict(lambda: -float("inf"))
        prevDp[(0, numCol - 1)] = grid[0][0] + grid[0][numCol - 1]

        for currRow in grid[1:]:
            currDp = defaultdict(lambda: -float("inf"))
            for i in range(numCol):
                for j in range(i, numCol):
                    currDp[(i, j)] = (currRow[i] + currRow[j] \
                        if i != j else currRow[i]) \
                        + max(prevDp[(i + di, j + dj)] \
                            for di in {-1, 0, 1}
                            for dj in {-1, 0, 1})
            prevDp = currDp

        return max(currDp.values())
