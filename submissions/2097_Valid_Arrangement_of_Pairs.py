class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        sLevel, eLevel = defaultdict(int), defaultdict(int)

        for pair in pairs:
            s, e = pair
            graph[s].append(e)
            sLevel[s] += 1
            eLevel[e] += 1
        
        results = []
        def travel(val: int):
            while graph[val]:
                nextVal = graph[val].popleft()
                travel(nextVal)
            results.append(val)

        curr = -1
        for val in sLevel.keys():
            if sLevel[val] == eLevel[val] + 1:
                curr = val
                break
        if curr == -1:
            curr = pairs[0][0]
        
        travel(curr)
        results.reverse()
        return [[s, e] for s, e in zip(results[:-1], results[1:])]

