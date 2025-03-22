class Solution:
    def countCompleteComponents(
        self, 
        n: int, 
        edges: List[List[int]],
    ) -> int:
        graph = defaultdict(list)
        for node in range(n):
            graph[node].append(node)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        comp2freq = defaultdict(int)
        for node in range(n):
            neighbors = tuple(sorted(graph[node]))
            comp2freq[neighbors] += 1


        return sum(
            1
            for neighbors, freq in comp2freq.items()
            if len(neighbors) == freq
        )

