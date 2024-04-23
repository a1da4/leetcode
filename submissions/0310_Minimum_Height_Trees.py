class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        if len(edges) == 1:
            return [0, 1]

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].ap   pend(edge[1])
            graph[edge[1]].append(edge[0])

        leafNodes = [nodeId for nodeId in range(n) if len(graph[nodeId]) == 1]

        while n > 2:
            n -= len(leafNodes)
            _leafNodes = []
            for leafNode in leafNodes:
                neighbor = graph[leafNode].pop()
                graph[neighbor].remove(leafNode)

                if len(graph[neighbor]) == 1:
                    _leafNodes.append(neighbor)
            leafNodes = _leafNodes

        return leafNodes

