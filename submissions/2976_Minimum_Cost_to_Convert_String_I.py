class Solution:
    def minimumCost(self, source: str, target: str, 
        original: List[str], changed: List[str], 
        cost: List[int]) -> int:
        
        def _ch2id(ch: str) -> int:
            return ord(ch) - ord('a')
        
        N = 26
        graph = [[float('inf')] * N for _ in range(N)]

        for i in range(N):
            graph[i][i] = 0
        
        for orig, chag, c in zip(original, changed, cost):
            graph[_ch2id(orig)][_ch2id(chag)] = min(graph[_ch2id(orig)][_ch2id(chag)], c)

        for via in range(N):
            for start in range(N):
                for end in range(N):
                    graph[start][end] = min(graph[start][end], graph[start][via] + graph[via][end])

        answer = 0
        for s, t in zip(source, target):
            if s != t:
                c = graph[_ch2id(s)][_ch2id(t)]
                if c == float('inf'):
                    return -1
                answer += c

        return answer
