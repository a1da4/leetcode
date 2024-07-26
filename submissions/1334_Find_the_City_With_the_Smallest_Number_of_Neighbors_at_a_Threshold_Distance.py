class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[float("inf")] * n for _ in range(n)]

        for i in range(n):
            graph[i][i] = 0
        
        for edge in edges:
            graph[edge[0]][edge[1]] = edge[2]
            graph[edge[1]][edge[0]] = edge[2]

        for via in range(n):
            for start in range(n):
                for end in range(n):
                    graph[start][end] = min(graph[start][end], 
                                            graph[start][via] + graph[via][end])

        minCount = float("inf")
        minIds = []

        for start in range(n):
            count = sum([graph[start][end] <= distanceThreshold \
                         for end in range(n)])

            if count == minCount:
                minIds.append(start)
            elif count < minCount:
                minCount = count
                minIds = [start]

        return minIds[-1]

