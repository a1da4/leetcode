class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # if the given graph have circuits -> False
        graph = {node: [] for node in range(n)}
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        queue = deque([(None, 0)])
        visited = set()
        visited.add(0)
        while queue:
            L = len(queue)
            for _ in range(L):
                parent, child = queue.popleft()
                
                for grandchild in graph[child]:
                    if grandchild in visited:
                        if grandchild != parent:
                            return False
                        else:
                            continue
                    queue.append((child, grandchild))
                    visited.add(grandchild)
                    
        return len(visited) == n

