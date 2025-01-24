class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        degree = [0] * N
        dest = [[] for _ in range(N)]
        for node in range(N):
            for neighbor in graph[node]:
                dest[neighbor].append(node)
                degree[node] += 1
        
        queue = deque()
        for node in range(N):
            if degree[node] == 0:
                queue.append(node)
        
        isSafe = [False] * N
        while queue:
            node = queue.popleft()
            isSafe[node] = True

            for neighbor in dest[node]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)

        return [node for node in range(N) if isSafe[node]]

