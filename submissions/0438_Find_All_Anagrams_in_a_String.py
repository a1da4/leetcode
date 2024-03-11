class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        K = len(p)
        pC = Counter(p)
        startIds = []
        if N < K:
            return startIds

        currWords = "_" + s[:K-1]
        for startId in range(N - K + 1):
            currWords = currWords[1:] + s[startId + K - 1]
            if Counter(currWords) == pC:
                startIds.append(startId)
        
        return startIds
