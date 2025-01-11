class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        N = len(s)
        if N < k:
            return False
        if N == k:
            return True
        
        l = 0
        for freq in Counter(s).values():
            if freq % 2:
                l += 1
        
        return l <= k

