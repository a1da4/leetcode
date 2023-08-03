class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numNodes = len(isConnected)
        numComponents = 0
        visited = [False] * numNodes

        def dfs(node, isConnected, visited):
            visited[node] = True
            for i in range(len(isConnected)):
                if isConnected[node][i] and not visited[i]:
                    dfs(i, isConnected, visited)
        

        for i in range(numNodes):
            if not visited[i]:
                numComponents += 1
                dfs(i, isConnected, visited)

        return numComponents
