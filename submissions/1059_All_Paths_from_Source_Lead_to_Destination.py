class Solution:
    def __init__(self):
        self.WIP = 1
        self.DONE = 2

    def _buildGraph(self, n, edges):
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            
        return graph
        
    def _leadsToDest(self, graph, node, dest, states):
        if states[node] is not None:
            return states[node] == self.DONE
        if len(graph[node]) == 0:
            return node == dest
        states[node] = self.WIP
        
        for next_node in graph[node]:
            if not self._leadsToDest(graph, next_node, dest, states):
                return False
        
        states[node] = self.DONE
        return True
    
    def leadsToDestination(self, n: int, edges: List[List[int]], 
        source: int, destination: int
        ) -> bool:
        graph = self._buildGraph(n, edges)
        return self._leadsToDest(graph, source, destination, [None] * n)
