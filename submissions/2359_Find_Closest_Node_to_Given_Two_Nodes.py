class Solution:
    INF = float('inf')
    def closestMeetingNode(
        self, 
        edges: List[int],
        node1: int,
        node2: int,
    ) -> int:
        answer = -1
        n = len(edges)
        dists1 = self.computeDist(edges, node1)
        dists2 = self.computeDist(edges, node2)
        preMax = self.INF
        for i in range(n):
            currMax = max(dists1[i], dists2[i])
            if (currMax != self.INF and currMax < preMax):
                preMax = currMax
                answer = i
         
        return answer
    
    def computeDist(
        self,
        edges: List[int],
        start: int,
    ) -> List[int]:
        n = len(edges)
        dists = [self.INF] * n
        queue = deque([start])
        dist = 0
        visited = set()
        while queue:
            L = len(queue)
            for _ in range(L):
                node = queue.popleft()
                dists[node] = dist
                visited.add(node)

                if edges[node] != -1:
                    if edges[node] in visited:
                        continue
                    else:
                        queue.append(edges[node])

            dist += 1
        
        return dists

