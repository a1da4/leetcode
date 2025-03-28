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
        passed = set()

        heap = [(grid[0][0], 0, 0)]
        heapq.heapify(heap)

        point = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for query in uniqQueries:
            while heap:
                currVal, currRow, currCol = heapq.heappop(heap)
                if (currRow, currCol) in passed:
                    continue
                
                if currVal < query:
                    passed.add((currRow, currCol))
                    point += 1
                    for direction in directions:
                        nextRow = currRow + direction[0]
                        nextCol = currCol + direction[1]
                        if (0 <= nextRow < numRow
                            and 0 <= nextCol < numCol
                            and (nextRow, nextCol) not in passed):
                            heapq.heappush(heap, (grid[nextRow][nextCol], nextRow, nextCol))
                else:
                    heapq.heappush(heap, (grid[currRow][currCol], currRow, currCol))
                    break

            for queryId in query2ids[query]:
                answer[queryId] = point
        
        return answer


