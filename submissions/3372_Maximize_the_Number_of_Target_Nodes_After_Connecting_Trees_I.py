class Solution:
    def countNodesDistK(
        self,
        n: int,
        edges: List[List[int]],
        k: int,
    ) -> List[int]:
        counts = [0] * n
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        for i in range(n):
            dist = 0
            count = 0
            queue = deque([i])
            visited = set()
            while queue:
                L = len(queue)
                for _ in range(L):
                    node = queue.popleft()
                    visited.add(node)
                    count += 1
                    for _node in graph[node]:
                        if _node in visited:
                            continue
                        queue.append(_node)
                dist += 1
                if dist > k:
                    break
            
            counts[i] = count
        
        return counts

    def maxTargetNodes(
        self, 
        edges1: List[List[int]], 
        edges2: List[List[int]], 
        k: int,
    ) -> List[int]:
        
        counts1 = self.countNodesDistK(
            len(edges1) + 1,
            edges1,
            k,
        )
        count2 = max(self.countNodesDistK(
            len(edges2) + 2,
            edges2,
            k - 1,
        ))

        answer = []
        for count in counts1:
            if k > 0:
                count += count2
            answer.append(count)

        return answer    
