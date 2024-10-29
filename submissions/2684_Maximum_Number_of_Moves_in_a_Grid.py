class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        answer = -1
        numRow, numCol = len(grid), len(grid[0])

        queue = deque([(r, 0) for r in range(numRow)])
        visited = set()
        while queue:
            N = len(queue)
            for _ in range(N):
                pos = queue.popleft()
                if pos not in visited:
                    visited.add(pos)
                    r, c = pos

                    if r - 1 >= 0 and c + 1 < numCol and \
                        grid[r][c] < grid[r - 1][c + 1]:
                        queue.append((r - 1, c + 1))
                    
                    if c + 1 < numCol and grid[r][c] < grid[r][c + 1]:
                        queue.append((r, c + 1))
                    
                    if r + 1 < numRow and c + 1 < numCol and \
                        grid[r][c] < grid[r + 1][c + 1]:
                        queue.append((r + 1, c + 1))
                
            answer += 1

        return answer

