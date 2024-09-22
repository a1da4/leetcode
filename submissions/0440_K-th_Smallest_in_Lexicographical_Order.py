class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def countSteps(prefix, n):
            steps = 0
            first = prefix
            next_prefix = prefix + 1
            while first <= n:
                steps += min(n + 1, next_prefix) - first
                first *= 10
                next_prefix *= 10
            return steps

        curr = 1
        k -= 1
        while k > 0:
            steps = countSteps(curr, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
                
        return curr

