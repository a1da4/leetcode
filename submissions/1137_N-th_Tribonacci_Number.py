class Solution:
    def tribonacci(self, n: int) -> int:

        def findTribonacci(n: int, d: Dict[int, int]) -> int:
            if n in d:
                return d[n]
            else:
                d[n] = findTribonacci(n-1, d) + findTribonacci(n-2, d) + findTribonacci(n-3, d)
                return d[n]
        
        return findTribonacci(n, {0: 0, 1: 1, 2: 1})
