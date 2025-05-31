class Solution:
    def findSmallestSetOfVertices(
        self, 
        n: int, 
        edges: List[List[int]],
    ) -> List[int]:
        graph = defaultdict(list)
        isParent = [True] * n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            isParent[edge[1]] = False

        answer = [node for node in range(n) if isParent[node]]

        return answer
   
