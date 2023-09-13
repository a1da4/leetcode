class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        numCitations = len(citations)

        h = 0
        for i, citation in enumerate(citations):
            if (numCitations - i) >= citation:
                h = max(h, citation)

            elif citation >= (numCitations - i):
                h = max(h, numCitations - i)
            
        return h
