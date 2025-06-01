class Solution:
    def networkRank(
        self,
        graph: Dict[int, int],
        connected: Dict[Tuple[int], bool],
        node1: int,
        node2: int,
    ) -> int:
        rank = graph[node1] + graph[node2]
        if connected[(node1, node2)]:
            rank -= 1

        return rank

    def maximalNetworkRank(
        self, 
        n: int, 
        roads: List[List[int]],
    ) -> int:
        answer = 0

        graph = defaultdict(int)
        connected = defaultdict(bool)
        for road in roads:
            graph[road[0]] += 1
            graph[road[1]] += 1
            connected[(road[0], road[1])] = True
            connected[(road[1], road[0])] = True
        
        for i in range(n):
            for j in range(i + 1, n):
                rank = self.networkRank(graph, connected, i, j)
                answer = max(answer, rank)
        
        return answer

