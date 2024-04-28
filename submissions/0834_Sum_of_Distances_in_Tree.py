class Solution:
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    answer = [0] * n
    nodes = [1] * n

    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    def dfs(node: int, parent: int = None):
        for child in graph[node]:
            if child == parent:
                continue
            dfs(child, node)
            nodes[node] += nodes[child]
            answer[node] += answer[child] + nodes[child]

    def update(node: int, parent: int = None):
        for child in graph[node]:
            if child == parent:
                continue
            answer[child] = answer[node] - nodes[child] + (n - nodes[child])
            update(child, node)

    dfs(0)
    update(0)
    
    return answer

