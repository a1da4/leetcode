class Solution:
    def canReach(
        self, 
        arr: List[int], 
        start: int,
    ) -> bool:
        N = len(arr)
        visited = set()
        queue = deque([start])
        while queue:
            L = len(queue)
            for _ in range(L):
                node = queue.popleft()
                if arr[node] == 0:
                    return True
                visited.add(node)

                for neighbour in [node + arr[node], node - arr[node]]:
                    if neighbour in visited:
                        continue
                    if 0 > neighbour or neighbour >= N:
                        continue
                    queue.append(neighbour)

        return False
        
