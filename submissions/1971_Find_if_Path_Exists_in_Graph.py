class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        if [source, destination] in edges or [destination, source] in edges:
            return True

        if not edges:
            return False
        
        src2dst = defaultdict(list)
        for edge in edges:
            src2dst[edge[0]].append(edge[1])
            src2dst[edge[1]].append(edge[0])
        
        self._visited = set()
        pathes = src2dst[source]
        while pathes:
            print(pathes)
            N = len(pathes)
            for _ in range(N):
                path = pathes.pop(0)
                if path in self._visited:
                    continue
                self._visited.add(path)
                if path == destination:
                    return True

                pathes += src2dst[path]

        return False

