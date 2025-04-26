class Solution:
    def allPathsSourceTarget(
        self, 
        graph: List[List[int]],
    ) -> List[List[int]]:
        goal = len(graph) - 1
        answer = []
        queue = deque([ (0, [0]) ])

        while queue:
            node, path = queue.popleft()
            if node == goal:
                answer.append(path)
            else:
                for nextNode in graph[node]:
                    queue.append(
                        (nextNode, path + [nextNode])
                    )

        return answer

