class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        answer = [[float("inf")] * n for _ in range(m)]

        visited = set()
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
                    queue.append((rId, cId, 0))
        while queue:
            L = len(queue)
            for _ in range(L):
                rId, cId, dist = queue.popleft()
                answer[rId][cId] = min(
                    answer[rId][cId],
                    dist,
                ) 
                visited.add((rId, cId))
                for direction in directions:
                    _rId, _cId = rId + direction[0], cId + direction[1]
                    if (0 <= _rId < m
                        and 0 <= _cId < n
                        and (_rId, _cId) not in visited):

                        if mat[_rId][_cId] == 0:
                            queue.append((_rId, _cId, 0))
                        else:
                            queue.append((_rId, _cId, dist + 1))

        return answer

