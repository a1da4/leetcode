class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        count = 0
        last = -float('inf')
        for s, e in pairs:
            if s > last:
                count += 1
                last = e

        return count

