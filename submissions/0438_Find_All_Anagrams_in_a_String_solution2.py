class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        N = len(s)
        K = len(p)
        pC = Counter(p)
        startIds = []
        if N < K:
            return startIds

        currWords = s[:K-1]
        currCounter = Counter(currWords)
        for startId in range(N - K + 1):
            currCounter.update(s[startId + K - 1])
            if currCounter == pC:
                startIds.append(startId)
            currCounter.subtract(s[startId])
        
        return startIds
