class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if citations[m] == n - m:
                return citations[m]
            elif citations[m] < n - m:
                l = m + 1
            else:
                r = m - 1

        return n - l

