class Solution:
    def decode(self, pathStr: str) -> List[int]:
        path = []
        for nodeStr in pathStr.split('-'):
            path.append(int(nodeStr))
        return path

    def allPathsSourceTarget(
        self, 
        graph: List[List[int]],
    ) -> List[List[int]]:
        goal = len(graph) - 1
        queue = deque([(0, '0')])
        visited = set()
        answer = []

        while queue:
            L = len(queue)
            for _ in range(L):
                node, pathStr = queue.popleft()
                visited.add(pathStr)

                if node == goal:
                    path = self.decode(pathStr)
                    answer.append(path)
                
                for nextNode in graph[node]:
                    nextPathStr = pathStr + '-' + str(nextNode)
                    if nextPathStr not in visited:
                        queue.append(
                            (nextNode, nextPathStr)
                        )

        return answer

