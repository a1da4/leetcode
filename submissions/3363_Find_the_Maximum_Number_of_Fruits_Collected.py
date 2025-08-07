class Solution:
    def search(
        self,
        fruits: List[List[int]],
        isBottomLeft: bool,
    ) -> int:
        n = len(fruits)

        for i in range(1, n):
            if isBottomLeft:
                cols = [fruits[x][i] for x in range(n)]
            else:
                cols = [fruits[i][y] for y in range(n)]
            for j in range(n - 1, n - 2 - i, -1):
                if j < i: continue
                if isBottomLeft:
                    x, y = j, i
                else:
                    x, y = i, j

                for d in [1, 0, -1]:
                    if isBottomLeft:
                        _x, _y = x + d, y - 1
                        if _x >= n or _x <= n - 1 - i: continue
                        fruits[x][y] = max(
                            fruits[x][y],
                            cols[x] + fruits[_x][_y],
                        )
                    else:
                        _x, _y = x - 1, y + d
                        if _y >= n or _y <= n - 1 - i: continue
                        fruits[x][y] = max(
                            fruits[x][y],
                            cols[y] + fruits[_x][_y],
                        )

        return fruits[n - 1][n - 1]

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)

        answer = 0
        for i in range(n):
            answer += fruits[i][i]
            fruits[i][i] = 0

        return answer + self.search([row[:] for row in fruits], True) + self.search([row[:] for row in fruits], False)
