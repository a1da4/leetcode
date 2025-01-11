class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo: Dict[Tuple[int, int, int], float] = {}
        directions = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
                      (1, -2), (2, -1), (2, 1), (1, 2)]

        def travel(rowId: int, colId: int, time: int) -> float:
            if not (0 <= rowId < n and 0 <= colId < n):
                return 0
            if time == 0:
                return 1

            if (rowId, colId, time) in memo:
                return memo[(rowId, colId, time)]

            curr = 0
            for dr, dc in directions:
                curr += 1 / 8 * travel(rowId + dr, colId + dc, time - 1)

            memo[(rowId, colId, time)] = curr
            return curr

        return travel(row, column, k)

