class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        M, N = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def is_valid(row: int, col: int) -> bool:
            return 0 <= row < M and 0 <= col < N and (row, col) not in visited

        heap = [(grid[0][0], 0, 0)]

        while heap:
            time, row, col = heapq.heappop(heap)

            if (row, col) == (M - 1, N - 1):
                return time

            if (row, col) in visited:
                continue
            visited.add((row, col))

            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy

                if not is_valid(next_row, next_col):
                    continue

                wait_time = (
                    1 if (grid[next_row][next_col] - time) % 2 == 0 else 0
                )
                next_time = max(grid[next_row][next_col] + wait_time, time + 1)
                heapq.heappush(heap, (next_time, next_row, next_col))

        return -1

