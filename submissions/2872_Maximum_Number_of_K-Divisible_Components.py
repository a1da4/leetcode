class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1

        numComponents = 0
        graph = defaultdict(list)
        numNodes = [0 for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            numNodes[node1] += 1
            numNodes[node2] += 1
        
        queue = deque([node for node in range(n) if numNodes[node] == 1])

        while queue:
            node = queue.popleft()
            numNodes[node] -= 1
            val = 0
            if values[node] % k == 0:
                numComponents += 1
            else:
                val = values[node]
            for neighbour in graph[node]:
                if numNodes[neighbour] == 0:
                    continue
                numNodes[neighbour] -= 1
                values[neighbour] += val

                if numNodes[neighbour] == 1:
                    queue.append(neighbour)
        
        return numComponents

