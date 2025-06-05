class Solution:
    def smallestEquivalentString(
        self, 
        s1: str, 
        s2: str, 
        baseStr: str,
    ) -> str:
        graph = defaultdict(list)
        for ch1, ch2 in zip(s1, s2):
            graph[ch1].append(ch2)
            graph[ch2].append(ch1)
    
        ch2ch = defaultdict(str)
        for ch in graph.keys():
            queue = deque([ch])
            visited = set()
            minCh = ch
            while queue:
                currCh = queue.popleft()
                visited.add(currCh)
                if minCh > currCh:
                    minCh = currCh
                for nextCh in graph[currCh]:
                    if nextCh in visited:
                        continue
                    queue.append(nextCh)
            ch2ch[ch] = minCh


        answer = ""
        for ch in baseStr:
            if ch in ch2ch:
                answer += ch2ch[ch]
            else:
                answer += ch
        
        return answer

