class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        heights = [[-1] * n for _ in range(m)]
        queue = deque()
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    queue.append((r, c))
                    heights[r][c] = 0
        
        currHeight = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            N = len(queue)
            for _ in range(N):
                r, c = queue.popleft()

                for direction in directions:
                    _r, _c = r + direction[0], c + direction[1]
                    if 0 <= _r < m and 0 <= _c < n and heights[_r][_c] == -1:
                        heights[_r][_c] = currHeight
                        queue.append((_r, _c))

            currHeight += 1

        return heights

