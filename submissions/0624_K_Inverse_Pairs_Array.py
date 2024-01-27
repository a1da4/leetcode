class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        function = {(1, 0): 1, (2, 0): 1, (2, 1): 1, (2, 2): 0, (3, 0): 1}
        mod = 10**9 + 7
        def f(n: int, k: int):
            if n == 0 or n * (n - 1) < k:
                return 0
            elif (n, k) in function:
                return function[(n, k)]
            elif k >= n:
                val = f(n - 1, k) + f(n, k - 1) - f(n - 1, k - n)
                val %= mod
                function[(n, k)] = val
                return val
            elif k >= 1:
                val = f(n - 1, k) + f(n, k - 1)
                val %= mod
                function[(n, k)] = val
                return val
            else:
                val = f(n - 1, k)
                val %= mod
                function[(n, k)] = val
                return val
        return f(n, k)
