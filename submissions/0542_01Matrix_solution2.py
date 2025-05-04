ass Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        answer = [[-1] * n for _ in range(m)]
        directions = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1],
        ]
        queue = deque([])
        for rId in range(m):
            for cId in range(n):
                if mat[rId][cId] == 0:
                    queue.append((rId, cId))
                    answer[rId][cId] = 0
        while queue:
            L = len(queue)
            for _ in range(L):
                rId, cId = queue.popleft()
                for direction in directions:
                    _rId, _cId = rId + direction[0], cId + direction[1]
                    if (0 <= _rId < m
                        and 0 <= _cId < n
                        and answer[_rId][_cId] == -1):
                        answer[_rId][_cId] = answer[rId][cId] + 1
                        queue.append((_rId, _cId))

        return answer

