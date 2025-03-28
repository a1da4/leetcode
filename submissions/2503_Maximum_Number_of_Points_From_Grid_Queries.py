class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        uniqQueries = sorted(list(set(queries)))
        query2ids = {}
        for queryId, query in enumerate(queries):
            if query not in query2ids:
                query2ids[query] = []
            query2ids[query].append(queryId)
        
        numRow, numCol = len(grid), len(grid[0])
        answer = [0] * len(queries)
        visited = set()
        notPassed = None
        point = 0

        for query in uniqQueries:
            queue = deque([(0, 0)]) if notPassed is None else deque(list(notPassed))
            notPassed = set()
            while queue:
                N = len(queue)
                for _ in range(N):
                    currRow, currCol = queue.popleft()
                    if (currRow, currCol) in visited or (currRow, currCol) in notPassed:
                        continue
                    
                    if grid[currRow][currCol] < query:
                        visited.add((currRow, currCol))
                        point += 1
                        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nextRow = currRow + direction[0]
                            nextCol = currCol + direction[1]
                            if (0 <= nextRow < numRow
                                and 0 <= nextCol < numCol
                                and (nextRow, nextCol) not in visited):
                                queue.append((nextRow, nextCol))
                    else:
                        notPassed.add((currRow, currCol))

            for queryId in query2ids[query]:
                answer[queryId] = point
        
        return answer


