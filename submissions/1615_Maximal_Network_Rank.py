class Solution:
    def networkRank(
        self,
        graph: List[List[int]],
        node1: int,
        node2: int,
    ) -> int:
        roads1 = set(graph[node1])
        roads2 = set(graph[node2])
        roads = roads1 | roads2

        return len(roads)

    def maximalNetworkRank(
        self, 
        n: int, 
        roads: List[List[int]],
    ) -> int:
        answer = 0

        graph = defaultdict(list)
        for node1, node2 in roads:
            road = f"{node1}-{node2}"
            graph[node1].append(road)
            graph[node2].append(road)
        
        for i in range(n):
            for j in range(i + 1, n):
                rank = self.networkRank(graph, i, j)
                answer = max(answer, rank)
        
        return answer
