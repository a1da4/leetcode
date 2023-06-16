class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n, k):
            print(f" - n: {n}, k: {k}")
            if n == 1:
                return 0
            length = 2**(n-1)
            mid = length // 2
            if k <= mid:
                return helper(n-1, k)
            else:
                return 1 - helper(n-1, k-mid)
        
        return helper(n, k)
