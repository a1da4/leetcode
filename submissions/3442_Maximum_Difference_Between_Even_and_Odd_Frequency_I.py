class Solution:
    def maxDifference(self, s: str) -> int:
        f1 = 0
        f2 = float('inf')
        for freq in Counter(s).values():
            if freq % 2:
                f1 = max(f1, freq)
            else:
                f2 = min(f2, freq)
        
        return f1 - f2
